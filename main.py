from src.astro_geo_info import astro_geo_info
import webbrowser

# Fetch the number of astronauts
url = "http://api.open-notify.org/astros.json"
result = astro_geo_info(url)

# Print detailed info
print(result)


webbrowser.open("src/iss.txt")