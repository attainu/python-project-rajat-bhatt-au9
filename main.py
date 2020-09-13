
import requests
import time
from datetime import datetime

class BitcoinNotification:
    def __init__(self, Bitcoin_Api_URL, Webhooks_URL):
        self.Bitcoin_Api_URL = Bitcoin_Api_URL
        self.Webhooks_URL = Webhooks_URL

    def getBitcoinPrice(self):
        api_url = self.Bitcoin_Api_URL
        response = requests.get(api_url)
        json_response = response.json()
        currentBitcoinPrice = json_response['bpi']['INR']['rate_float']
        #print(currentBitcoinPrice)
        return currentBitcoinPrice


    def postWebhooks(self, event, value):
        data = {'value1':value}
        ifttt_event_url  = self.Webhooks_URL.format(event)
        requests.post(ifttt_event_url, json=data)
    

    def sendIFTTTEmergencyNotificaton(self):
        #bitcoin_history = []
        price = self.getBitcoinPrice()
        date = datetime.now()
        #bitcoin_history.append({'date': date, 'price': price})
        self.postWebhooks('bitcoin_price_emergency', price)

    def sendTelegramNotificaton(self):
        #bitcoin_history = []
        price = self.getBitcoinPrice()
        date = datetime.now()
        #bitcoin_history.append({'date': date, 'price': price})
        self.postWebhooks('bitcoin_price_update', price)
        time.sleep(5 * 60)  # Sleep for 5 minutes



if __name__ == "__main__":
    Bitcoin_Api_URL = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
    Webhooks_URL = 'https://maker.ifttt.com/trigger/{}/with/key/no2QXAKRWEMzu572PNeau5QTtIA3TrOrm4oRjtBLLY6'

    b1 = BitcoinNotification(Bitcoin_Api_URL,Webhooks_URL)
    b1.getBitcoinPrice()
    #b1.sendIFTTTEmergencyNotificaton()
    b1.sendTelegramNotificaton()