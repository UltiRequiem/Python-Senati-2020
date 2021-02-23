import requests
import json
from tabulate import *
from my_apic_em_functions import *

def run():
    api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {"content-type":"application/json",
            "X-Auth-Token": ticket}
    resp = requests.get(api_url, headers= headers, verify=False)
    print("Estado de la solicitud /host: ", resp.status_code)
    if resp.status_code != 200:
        raise Exception("Codigo de estado no es igual a 200. Respuesta de texto: " + resp.text)
    response_json = resp.json()
    device_list = []
    i = 0
    for item in response_json["response"]:
        i += 1
        device = [i, item["type"], item["managementIpAddress"]]
        device_list.append(device)
    table_header = ["Number", "Type", "IP"]
    print(tabulate(device_list, table_header))

if __name__ == '__main__':
    run()