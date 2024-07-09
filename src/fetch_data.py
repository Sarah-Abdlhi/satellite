import json
import urllib.request
import time

# Function to fetch data from a URL with retries
def fetch_data(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = urllib.request.urlopen(url)
            return json.loads(response.read())
        except Exception as e:
            print(f"Error fetching data: {e}")
            if i < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise