import urllib.parse
import requests

def run():
    url='https://maps.googleapis.com/maps/api/geocode/json?address=Alfredo+mendiola+3540,+CA&key=AIzaSyC5guRUsYSgt9ADNt5LCOOoHc9p48oG2io'
    json_data = requests.get(url).json()
    country = json_data['results'][0]['address_components'][5]['long_name']
    print(country)

if __name__ == '__main__':
    run()