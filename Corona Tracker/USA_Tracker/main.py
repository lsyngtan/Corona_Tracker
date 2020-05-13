import json 
import threading
import http.client
from USA_Cases import getting_usa_value, stupid_test
from pprint import pprint

# Configuration section
UBEAC_URL = 'hub.ubeac.io'
GATEWAY_URL = 'http://coronavirus.hub.ubeac.io/covid19'
DEVICE_FRIENDLY_NAME_2 = 'My USA COVID19 Tracker 2.0'
SENT_INTERVAL = 10 # Sent data interval in second

def main():
    threading.Timer(SENT_INTERVAL, main).start()
    device_usa = [{
        'id': DEVICE_FRIENDLY_NAME_2,
        'sensors': getting_usa_value()
        }]  

    connection = http.client.HTTPSConnection(UBEAC_URL)
    connection.request('POST', GATEWAY_URL, json.dumps(device_usa))
    response = connection.getresponse()
    print(response.read().decode())           

if __name__ == '__main__':
    main()