from src.astro_info import astro_info
from src.geo_info import geo_info
import webbrowser
import json

# Fetch the number of astronauts
url = "http://api.open-notify.org/astros.json"

geo_info()
astro_info(url)

webbrowser.open("src/iss.txt")