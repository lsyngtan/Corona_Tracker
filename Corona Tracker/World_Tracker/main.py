import json 
import threading
import http.client
from World_Cases import getting_world_value

# Configuration section
UBEAC_URL = 'hub.ubeac.io'
GATEWAY_URL = 'http://coronavirus.hub.ubeac.io/covid19'
DEVICE_FRIENDLY_NAME_1 = 'World COVID19 Tracker'
SENT_INTERVAL = 900 # Sent data interval in second

day = False
date = input("Update for Today or Yesterday? (T/Y) : ")
if date == 'T':
    day = True
else:
    day = False

def main():
    threading.Timer(SENT_INTERVAL, main).start()
    device_world = [{
        'id': DEVICE_FRIENDLY_NAME_1,
        'sensors': getting_world_value(day)
        }]    

    connection = http.client.HTTPSConnection(UBEAC_URL)
    connection.request('POST', GATEWAY_URL, json.dumps(device_world))
    response = connection.getresponse()
    print(response.read().decode())           

if __name__ == '__main__':
    main()