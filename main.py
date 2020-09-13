
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
        return round(currentBitcoinPrice,2)


    def postWebhooks(self, event, value):
        ifttt_event_url  = self.Webhooks_URL.format(event)
        requests.post(ifttt_event_url, json=value)
    

    def sendIFTTTEmergencyNotificaton(self):
        price = self.getBitcoinPrice()
        value = {'value1': price}
        self.postWebhooks('bitcoin_price_emergency', value)

    def sendTelegramNotificaton(self):
        
        price = self.getBitcoinPrice()
        value = {'value1': price}
        self.postWebhooks('bitcoin_price_update', value)
        
        #time.sleep(5 * 60)  # Sleep for 5 minutes

    def sendGmailNotification(self):

        name = input('Please enter your name: ')
        email = input('Please enter your Email: ')
        price = self.getBitcoinPrice()
        
        value = {'value1':email, 'value2':name, 'value3': price}
        
        self.postWebhooks('email_notification', value)






if __name__ == "__main__":
    Bitcoin_Api_URL = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
    Webhooks_URL = 'https://maker.ifttt.com/trigger/{}/with/key/no2QXAKRWEMzu572PNeau5QTtIA3TrOrm4oRjtBLLY6'

    b1 = BitcoinNotification(Bitcoin_Api_URL,Webhooks_URL)
    
    b1.sendIFTTTEmergencyNotificaton()
    #b1.sendTelegramNotificaton()
    #b1.sendGmailNotification()