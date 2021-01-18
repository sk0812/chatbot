import webbrowser

def search_amazon(text):
    if "for" in text:
        text = text.split("for ",1)[1]
    else:
        text = input("What would you like to search amazon for? (Type cancel to cancel the search!): ")
    if text.lower() == "cancel":
        pass
    else:
        url = (f"https://www.amazon.co.uk/s?k={text}")
        webbrowser.open(url, new = 2)
