import webbrowser

def search_ebay(text):
    if "for" in text:
        text = text.split("for ",1)[1]
    else:
        text = input("What would you like to search ebay for? (Type cancel to cancel the search!): ")
    if text.lower() == "cancel":
        pass
    else:
        url = (f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={text}")
        webbrowser.open(url, new = 2)
