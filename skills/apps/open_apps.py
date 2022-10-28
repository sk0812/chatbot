import sys
sys.path.insert(1, "skills/apps")

from apps import *

import random
import os

from output import output

def print_res(app):
    responses = [f"Okay sir, opening {app}", f"opening {app}, sir",
                 f"Okay sir, I am opening {app}"]
    response = random.choice(responses)
    output(response)

def open_app(tag):
    if tag == "open_spotify":
        os.system(f"open {spotify}")
        print_res("spotify")
    elif tag == "open_discord":
        os.system(f"open {discord}")
        print_res("discord")
    elif tag == "open_spark":
        os.system(f"open {spark}")
        print_res("spark")
    elif tag == "open_adobe_illustrator":
        os.system(f"open {adobe_illustrator}")
        print_res("adobe illustrator")
    elif tag == "open_adobe_photoshop":
        os.system(f"open {adobe_photoshop}")
        print_res("adobe photoshop")
    elif tag == "open_adobe_premiere":
        os.system(f"open {adobe_premiere}")
        print_res("adobe premiere")
    elif tag == "open_brave":
        os.system(f"open {brave}")
        print_res("brave")
    elif tag == "open_excel":
        os.system(f"open {excel}")
        print_res("excel")
    elif tag == "open_onenote":
        os.system(f"open {onenote}")
        print_res("onenote")
    elif tag == "open_powerpoint":
        os.system(f"open {powerpoint}")
        print_res("powerpoint")
    elif tag == "open_word":
        os.system(f"open {word}")
        print_res("word")
    elif tag == "open_outlook":
        os.system(f"open {outlook}")
        print_res("outlook")
    elif tag == "open_teams":
        os.system(f"open {teams}")
        print_res("teams")
    elif tag == "open_whatsapp":
        os.system(f"open {whatsapp}")
        print_res("whatsapp")
    elif tag == "open_proton_vpn":
        os.system(f"open {proton_vpn}")
        print_res("proton vpn")
    elif tag == "open_notion":
        os.system(f"open {notion}")
        print_res("notion")
    elif tag == "open_ccleaner":
        os.system(f"open {ccleaner}")
        print_res("ccleaner")
    elif tag == "open_qbittorent":
        os.system(f"open {qbittorent}")
        print_res("qbittorent")