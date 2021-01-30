from train import response, classify, intents
from skill_import import skills, run_skills, websites, run_open_websites
import random

context = {}
inputs = []
non_context = ["greeting", "thanks", "okay", "no_okay"]
while True:
    text = input("You: ")
    if classify(text):
        tag = classify(text)[0][0]
        val = classify(text)[0][1]
        inputs.append(text)
        if len(inputs) > 2:
            inputs.pop(0)
        if len(inputs) == 2:
            input_1 = inputs[0]
            input_1_tag = classify(input_1)[0][0]
            for i in intents['intents']:
                if i['tag'] == input_1_tag:
                    if "context_set" in i:
                        if isinstance(i['context_set'], list):
                            input_1_context = []
                            for item in i['context_set']:
                                input_1_context.append(item)
                        else:
                            input_1_context = i['context_set']
                        check_context_set = True
                    else:
                        check_context_set = False
                if i['tag'] == tag:
                    if "context_filter" in i:
                        if isinstance(i['context_filter'], list):
                            input_2_context = []
                            for item in i['context_filter']:
                                input_2_context.append(item)
                        else:
                            input_2_context = i['context_filter']
                        check_context_filter = True
                    else:
                        check_context_filter = False
        else:
            check_context_set = False
            check_context_filter = False
        if val > 0.85:
            if check_context_set and check_context_filter is True:
                if input_1_context in input_2_context:
                    if tag in skills:
                        run_skills(tag, text)
                    elif tag in websites:
                        run_open_websites(tag)
                    else:
                        print(response(text, context))
            else:
                if tag in skills:
                    run_skills(tag, text)
                elif tag in websites:
                    run_open_websites(tag)
                elif tag == "goodbye":
                    print(response(text, context))
                    break
                else:
                    if tag in non_context:
                        pass
                    else:
                        context = {}
                    print(response(text, context))
        else:
            responses = ["Sorry sir, I can't do that just yet", "Sorry sid, I am unable to do that just yet", "Sorry sir, I don't understand", "Sorry sir, I don't understand that but I am learning every day", "I haven't been trained to do that just yet, but I am learning every day"]
            print(random.choice(responses))