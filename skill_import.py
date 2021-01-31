from skills.weather.current_temp import current_temp
from skills.weather.current_weather import current_weather
from skills.weather.today_weather import today_weather
from skills.weather.tomorrow_weather import tomorrow_weather
from skills.weather.tonight_weather import tonight_weather
from skills.misc.dice_roll import dice_roll
from skills.misc.coin_flip import coin_flip
from skills.websites.open_websites import open_websites
from skills.misc.day import day
from skills.misc.time import time
from skills.misc.what_can_you_do import what_can_you_do
from skills.search.search_google import search_google
from skills.search.search_youtube import search_youtube
from skills.search.search_amazon import search_amazon
from skills.search.search_ebay import search_ebay
from skills.misc.random_number import random_number
from skills.misc.joke import joke
from skills.terminal import clear

skills = ["current_weather", "current_weather_context", "today_weather", "today_weather_context", "tomorrow_weather", "tomorrow_weather_context","dice_roll", "coin_flip", "day", "time", "what_can_you_do", "search_google", "search_amazon", "search_ebay", "search_youtube","random_number", "joke", "tonight_weather", "current_temp", "clear_cmd"]

websites = ["open_youtube", "open_habsnet", "open_outlook", "open_smhw", "open_amazon", "open_ebay", "open_gmail", "open_bbc_bitesize", "open_google", "open_github", "open_google_drive", "open_imdb", "open_reddit", "open_netflix", "open_wikipedia"]

def run_skills(tag, text):
    if tag == "current_temp":
        current_temp()
    elif tag == "current_weather":
        current_weather()
    elif tag == "current_weather_context":
        current_weather()
    elif tag == "today_weather":
        today_weather()
    elif tag == "today_weather_context":
        today_weather()
    elif tag == "tomorrow_weather":
        tomorrow_weather()
    elif tag == "tomorrow_weather_context":
        tomorrow_weather()
    elif tag == "tonight_weather":
        tonight_weather()
    elif tag == "dice_roll":
        dice_roll()
    elif tag == "coin_flip":
        coin_flip()
    elif tag == "day":
        day()
    elif tag == "time":
        time()
    elif tag == "what_can_you_do":
        what_can_you_do()
    elif tag == "search_google":
        search_google(text)
    elif tag == "search_youtube":
        search_youtube(text)
    elif tag == "search_amazon":
        search_amazon(text)
    elif tag == "search_ebay":
        search_ebay(text)
    elif tag == "random_number":
        random_number(text)
    elif tag == "joke":
        joke()
    elif tag == "clear_cmd":
        cls()


def run_open_websites(tag):
    open_websites(tag)
