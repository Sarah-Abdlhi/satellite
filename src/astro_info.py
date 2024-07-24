from src.fetch_data import fetch_data
import geocoder


def astro_info(url):

    # Fetch the number of astronauts
    result = fetch_data(url)

    with open("src/iss.txt", "w") as file:
        file.write("There are currently " +
                str(result["number"]) + " astronauts on the ISS: \n\n")
        people = result["people"]
        for p in people:
            file.write(p['name'] + " - on board" + "\n")

    # Convert the result dictionary to a JSON string
    result_json = json.dumps(result, indent=4)
    # Print detailed info
    print(result_json)

    