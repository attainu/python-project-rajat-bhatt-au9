# Bitcoin Price Notification

# Description

This is a python package which is used to give regular notifications on different platforms like  email,telegram and IFTTT app notifications. 

Main aim is to give notification on selected platform on regular intervals which can be set according to the user, by default which is 1 minute and also user can set threshold price which is set to ₹4,00,000 by default.


![Image of Bitcoin](https://cdn.pixabay.com/photo/2016/11/10/05/09/bitcoin-1813503_960_720.jpg)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bitcoin notification package.

```bash
pip install bitcoin-notifier-rajatbhatt500
```

## Prerequisite
To use this package one should have below things:

* install the IFTTT App to receive the emergency notifications
* An Email account to get notification.
* Telegram App and must join this channel.click the [Telegram channel](https://t.me/bitcoin_notificationrajat) to join the channel.

## Usage
For Help Menu

```bash
bitcoin-notification --help
```

You'll see below message in command line
```bash
usage:             Usage: This app gives the price of 1 Bitcoin in INR.
            Destination(-d) must be provided else destination will be
            telegram by default.
            To recive notification from IFTTT install IFTTT mobile app.
            To recive notifications on Telegram install Telegram app
            and join this channel https://t.me/bitcoin_notificationrajat .

            Prerequisite : INSTALL IFTTT APP AND TELEGRAM APP
            and TO RECIVE NOTIFICATON.
            PRESS Ctrl+C to terminate the app


BITCOIN PRICE NOTIFIER

optional arguments:
  -h, --help            show this help message and exit
  -i interval, --interval interval
                        Time interval in minutes
  -t threshold, --threshold threshold
                        Threshold in INR(₹)
  -d destnation, --destination destnation
                        There are various options to recive notificationsfrom us (1)IFTTT app (2) Telegram app (3)
                        Email

Copyright @Rajat Bhatt
```
To here the example for notification in telegram:
```bash
bitcoin-notification -t 600000 -i 2 -d telegram
```

## License
[MIT](https://choosealicense.com/licenses/mit/)