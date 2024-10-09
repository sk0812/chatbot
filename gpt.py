import ollama


def gpt_output(text):
    stream = ollama.chat(
        model='dolphin-llama3',
        messages=[{'role': 'user', 'content': text}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)