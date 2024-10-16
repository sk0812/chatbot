from train import response, classify, intents
from skill_import import skills, run_skills, websites, apps, run_open_websites, run_open_apps
import random
from speak import speak
from output import output
from gpt import gpt_output

context = {}
inputs = []
non_context = ["clear_cmd", "cwd_cmd"]
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
        if val > 0.95:
            if check_context_set and check_context_filter is True:
                if input_1_context in input_2_context:
                    if tag in skills:
                        run_skills(tag, text)
                    elif tag in websites:
                        run_open_websites(tag)
                    elif tag in apps:
                        run_open_apps(tag)
                    else:
                        output(response(text, context))
            else:
                if tag in skills:
                    run_skills(tag, text)
                elif tag in websites:
                    run_open_websites(tag)
                elif tag in apps:
                    run_open_apps(tag)
                else:
                    if tag not in non_context:
                        context = {}
                    output(response(text, context))
        else:
            gpt_output(text)
            print("")
        print(val)