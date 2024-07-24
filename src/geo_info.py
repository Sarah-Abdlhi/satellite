
import geocoder

def geo_info():

    with open("src/iss.txt", "w") as file:
        
        # Handle geolocation gracefully
        try:
            g = geocoder.ip('me')
            file.write("\nYour current lat / long is: " + str(g.latlng))
        except Exception as e:
            print(f"Geolocation error: {e}")
            file.write("\nYour current lat / long could not be determined.")