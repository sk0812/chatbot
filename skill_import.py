from skills.weather.current_temp import current_temp
from skills.weather.current_weather import current_weather
from skills.weather.today_weather import today_weather
from skills.weather.tomorrow_weather import tomorrow_weather
from skills.weather.tonight_weather import tonight_weather
from skills.websites.open_websites import open_websites
from skills.apps.open_apps import open_app
from skills.misc.day import day
from skills.misc.time import time
from skills.search.search_google import search_google
from skills.search.search_youtube import search_youtube
from skills.search.search_amazon import search_amazon
from skills.search.search_ebay import search_ebay
from skills.terminal.clear import clear
from skills.terminal.cwd import cwd
from skills.todo_list.add_item import add_item_todo_list

from output import start_talking, stop_talking


skills = ["current_weather", "current_weather_context", "today_weather", "today_weather_context", "tomorrow_weather", "tomorrow_weather_context","dice_roll", "coin_flip", "day", "time", "what_can_you_do", "search_google", "search_amazon", "search_ebay", "search_youtube","random_number", "joke", "another_joke", "tonight_weather", "current_temp", "clear_cmd", "cwd_cmd", "add_item_todo_list", "stop_talking", "start_talking"]

websites = ["open_youtube", "open_habsnet", "open_outlook", "open_smhw", "open_amazon", "open_ebay", "open_gmail", "open_bbc_bitesize", "open_google", "open_github", "open_google_drive", "open_imdb", "open_reddit", "open_netflix", "open_wikipedia"]

apps = ["open_spotify", "open_discord", "open_spark", "open_adobe_illustrator", "open_adobe_photoshop", "open_adobe_premiere", "open_brave", "open_excel", "open_onenote", "open_powerpoint", "open_word", "open_outlook", "open_teams", "open_whatsapp", "open_proton_vpn", "open_notion", "open_ccleaner", "open_qbittorent"]

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
    elif tag == "clear_cmd":
        clear()
    elif tag == "cwd_cmd":
        cwd()
    elif tag == "add_item_todo_list":
        add_item_todo_list(text)
    elif tag == "stop_talking":
        stop_talking()
    elif tag == "start_talking":
        start_talking()

def run_open_websites(tag):
    open_websites(tag)

def run_open_apps(tag):
    open_app(tag)