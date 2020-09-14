
import requests
import time
from datetime import datetime
import argparse
import sys

class BitcoinNotification:
    def __init__(self, Bitcoin_Api_URL, Webhooks_URL):
        self.Bitcoin_Api_URL = Bitcoin_Api_URL
        self.Webhooks_URL = Webhooks_URL

    def getBitcoinPrice(self):
        try:    
            api_url = self.Bitcoin_Api_URL
            response = requests.get(api_url)  
            json_response = response.json()
            currentBitcoinPrice = json_response['bpi']['INR']['rate_float']
            #print(currentBitcoinPrice)
            return round(currentBitcoinPrice,2)

        except requests.exceptions.RequestException:    # This is the correct syntax
            print(' NO Internet, Please check your Internet connection and rumn program again. ')
            sys.exit()
            
        


    def postWebhooks(self, event, value):
        ifttt_event_url  = self.Webhooks_URL.format(event)
        requests.post(ifttt_event_url, json=value)
    

    def sendIFTTTEmergencyNotificaton(self):
        price = self.getBitcoinPrice()
        
        value = {'value1': price}
        self.postWebhooks('bitcoin_price_emergency', value)
        print("Emergency notification sent")

    def sendTelegramNotificaton(self):
        
        price = self.getBitcoinPrice()
        
        value = {'value1': price}
        self.postWebhooks('bitcoin_price_update', value)
        print("Telegram Notification sent")
        
        #time.sleep(5 * 60)  # Sleep for 5 minutes

    def sendGmailNotification(self):

        name = input('Please enter your name: ')
        email = input('Please enter your Email: ')
        price = self.getBitcoinPrice()
        
        value = {'value1':email, 'value2':name, 'value3': price}
        self.postWebhooks('email_notification', value)
        print("Email notification sent")





if __name__ == "__main__":
    Bitcoin_Api_URL = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
    Webhooks_URL = 'https://maker.ifttt.com/trigger/{}/with/key/no2QXAKRWEMzu572PNeau5QTtIA3TrOrm4oRjtBLLY6'

    b1 = BitcoinNotification(Bitcoin_Api_URL,Webhooks_URL)
    current_bitcoinprice = b1.getBitcoinPrice()
    
##################################################################################################################


    parser = argparse.ArgumentParser(
    usage='''\
        Usage: This app gives the price of 1 Bitcoin in INR. 
        Destination(-d) must be provided else destination will be telegram by default.
        To recive notification from IFTTT install IFTTT mobile app. To recive notifications on 
        Telegram install Telegram app and join this channel @IFTTT.

        Prerequisite : INSTALL IFTTT APP AND TELEGRAM APP ON ANDROID/IOS/WINDOWS TO RECIVE NOTIFICATON. 
        PRESS Ctrl+C to terminate the app
        ''',
        description="Bitcoin price Notification",
        epilog="Copyrights @ Rajat Bhatt")
    # command line variable for time gap
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        nargs=1,
        metavar="interval",
        default=[1],
        help="Time interval in minutes")
    # command line variable for threshold
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        nargs=1,
        metavar="threshold",
        default=[400000],
        help="Threshold in INR(₹)")
        
    # command line variable for destination
    parser.add_argument(
        "-d",
        "--destination",
        metavar='destnation',
        default='telegram',
        help='There are various options to recive notifications from us (1)IFTTT app (2) Telegram app (3) Email')
    new_args = parser.parse_args()
    print('Running Application with time interval of ', new_args.interval[0],
        ' and threshold = ₹', new_args.threshold[0], 'and Destination = ',
        new_args.destination)
    # calls the function to send notifications
    if (new_args.destination == 'telegram' and new_args.threshold[0] < current_bitcoinprice):
        print('''\
            To recive the notification
        from Telegram, install the telegram app and join the
        channel @IFTTT
        ''')
        b1.sendTelegramNotificaton()
    
    if (new_args.destination == 'ifttt' or new_args.threshold[0] > current_bitcoinprice):
        b1.sendIFTTTEmergencyNotificaton()
    if (new_args.destination == 'email'):
        b1.sendGmailNotification()

