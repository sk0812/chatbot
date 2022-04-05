import webbrowser
import sys
import random
sys.path.insert(1, "skills/websites")
from websites import *

def print_res(website):
    responses = [f"Okay sir, opening {website}", f"opening {website}, sir",
                 f"Okay sir, I am opening {website} in your browser", f"opening {website} in your browser, sir"]
    print(random.choice(responses))


def open_websites(tag):
    if tag == "open_youtube":
        webbrowser.open(youtube, new=2)
        print_res("youtube")
    elif tag == "open_smhw":
        webbrowser.open(smhw, new=2)
        print_res("show my homework")
    elif tag == "open_amazon":
        webbrowser.open(amazon, new=2)
        print_res("amazon")
    elif tag == "open_ebay":
        webbrowser.open(ebay, new=2)
        print_res("ebay")
    elif tag == "open_gmail":
        webbrowser.open(gmail, new=2)
        print_res("gmail")
    elif tag == "open_bbc_bitesize":
        webbrowser.open(bbc_bitesize, new=2)
        print_res("bbc bitesize")
    elif tag == "open_google":
        webbrowser.open(google, new=2)
        print_res("google")
    elif tag == "open_github":
        webbrowser.open(github, new=2)
        print_res("github")
    elif tag == "open_google_drive":
        webbrowser.open(google_drive, new=2)
        print_res("google drive")
    elif tag == "open_imdb":
        webbrowser.open(imdb, new=2)
        print_res("imdb")
    elif tag == "open_reddit":
        webbrowser.open(reddit, new=2)
        print_res("reddit")
    elif tag == "open_netflix":
        webbrowser.open(netflix, new=2)
        print_res("netflix")
    elif tag == "open_wikipedia":
        webbrowser.open(wikipedia, new=2)
        print_res("wikipedia")
