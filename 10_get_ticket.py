import requests
import json
requests.packages.urllib3.disable_warnings()

def run():
    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    headers = {"content-type":"application/json"}
    body_json = {"password": "Cisco123!",
                "username": "devnetuser"
                }
    resp = requests.post(api_url, json.dumps(body_json), headers= headers, verify=False)
    """ print("Estado de la solicitud del ticket:", resp.status_code) """
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    print("El número del ticket de servicio es: ", serviceTicket)
 
if __name__ == '__main__':
    run()