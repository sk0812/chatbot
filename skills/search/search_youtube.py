import webbrowser

def search_youtube(text):
    if "for" in text:
        text = text.split("for ",1)[1]
    else:
        text = input("What would you like to search youtube for? (Type cancel to cancel the search!): ")
    if text.lower() == "cancel":
        pass
    else:
        url = (f"https://www.youtube.com/results?search_query={text}")
        webbrowser.open(url, new = 2)
