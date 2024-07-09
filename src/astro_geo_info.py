from src.fetch_data import fetch_data
import geocoder
import json

def astro_geo_info(url):

    # Fetch the number of astronauts
    result = fetch_data(url)

    with open("src/iss.txt", "w") as file:
        file.write("There are currently " +
                str(result["number"]) + " astronauts on the ISS: \n\n")
        people = result["people"]
        for p in people:
            file.write(p['name'] + " - on board" + "\n")
        
        # Handle geolocation gracefully
        try:
            g = geocoder.ip('me')
            file.write("\nYour current lat / long is: " + str(g.latlng))
        except Exception as e:
            print(f"Geolocation error: {e}")
            file.write("\nYour current lat / long could not be determined.")

    # Convert the result dictionary to a JSON string
    result_json = json.dumps(result, indent=4)
    return result_json