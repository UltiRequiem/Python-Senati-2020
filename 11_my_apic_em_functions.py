import requests
import json
from tabulate import *

requests.packages.urllib3.disable_warnings() # Desactiva SSL advertencias

def get_ticket():
   api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
   headers = {"content-type":"application/json"}
   body_json = {"username": "devnetuser",
                "password": "Cisco123!"}
   resp = requests.post(api_url, json.dumps(body_json), headers= headers, verify=False)
   status = resp.status_code) # el codigo de estado es una propiedad del objeto resp
   response_json = resp.json()
   serviceTicket = response_json["response"]["serviceTicket"]
   print("El número del ticket de servicio es: ", serviceTicket)
   return serviceTicket

def print_hosts():
   api_url = "https://sandboxapicem.cisco.com/api/v1/host"
   ticket = get_ticket()
   headers = {"content-type":"application/json",
              "X-Auth-Token": ticket}
   resp = requests.get(api_url, headers= headers, verify=False)
   response_json = resp.json()
   host_list = []
   i = 0
   for item in response_json["response"]:
       i += 1
       host = [i, item["hostType"], item["hostIp"]]
       host_list.append(host)
   table_header = ["Number", "Type", "IP"]
   print(tabulate(host_list, table_header))
