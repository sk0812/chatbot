import webbrowser

def search_google(text):
    if "for" in text:
        text = text.split("for ",1)[1]
    else:
        text = input("What would you like to search google for? (Type cancel to cancel the search!): ")
    if text.lower() == "cancel":
        pass
    else:
        url = (f"https://www.google.com/search?q={text}")
        webbrowser.open(url, new = 2)
