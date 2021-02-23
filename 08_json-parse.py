import urllib.parse
import requests

def run():
  main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
  key = 'AIzaSyC5guRUsYSgt9ADNt5LCOOoHc9p48oG2io'
  while  True:
    address = input("Address: ")
    if address == "quit" or address == "q":
      break
    url = main_api + urllib.parse.urlencode({"address":address,"key":key})
    json_data = requests.get(url).json()
    print(url)
    json_status = json_data["status"]
    print('Estado de API: ' + json_status + "\n")
    if json_status == "OK":
      for each in json_data["results"][0]["address_components"]:
          print(each["long_name"])
      formatted_address = json_data['results'][0]['formatted_address']
      print("\n" + formatted_address)

if __name__ == '__main__':
  run()
