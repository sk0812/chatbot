import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
import os

with open('intents.json') as json_data:
    intents = json.load(json_data)

words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each text in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the text
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each text
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training, dtype="object")

# create train and test lists
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

if os.path.exists("training_data"):
    # restore all of our data structures
    data = pickle.load(open("training_data", "rb"))
    words = data['words']
    classes = data['classes']
    train_x = data['train_x']
    train_y = data['train_y']

    # import our chat-bot intents file
    with open('intents.json') as json_data:
        intents = json.load(json_data)

    # load our saved model
    model.load("model.tflearn")

else:
    # reset underlying graph data
    tf.compat.v1.reset_default_graph()
    model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
    model.save('model.tflearn')

    # save all of our data structures
    pickle.dump({'words': words, 'classes': classes, 'train_x': train_x,
                 'train_y': train_y}, open("training_data", "wb"))


def clean_up_text(text):
    # tokenize the pattern
    text_words = nltk.word_tokenize(text)
    # stem each word
    text_words = [stemmer.stem(word.lower()) for word in text_words]
    return text_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the text


def bow(text, words, show_details=False):
    # tokenize the pattern
    text_words = clean_up_text(text)
    # bag of words
    bag = [0] * len(words)
    for s in text_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    return ("found in bag: %s" % w)

    return(np.array(bag))


ERROR_THRESHOLD = 0.5


def classify(text):
    # generate probabilities from the model
    results = model.predict([bow(text, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


def response(text, context, userID='123', show_details=False):
    results = classify(text)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details:
                            return ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                            (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details:
                            return ('tag:', i['tag'])
                        # a random response from the intent
                        return random.choice(i['responses'])

            results.pop(0)
