# Smishing

The Smishing purpose is to be able to track SMS Phishing message with the Phishing Frenzy project. When a victim click on the link in the SMS, it will be tracked in Phishing Frenzy. Smishing will send SMS to the list of target. 

![smishing](https://user-images.githubusercontent.com/838845/80989277-b8385600-8e02-11ea-84b3-a156c5fd804a.gif)



## How to use smishing.py
First, you will need to create a smishing.conf file in the root smishing folder. 

```
{
    "recovery": true,
    "savedRecoveryFileName": "recovery.list",
    "cost": 0.0075,
    "sleep": 2.0,
    "senderPhoneNumber": "",
    "useColor": true,
    "loggingLevel": "info",
    "loggingFileName": "sendtest.log",
    "savedVictimFileName": "victims.list",
    "TWILIO_AUTH_TOKEN": null,
    "TWILIO_ACCOUNT_SID": null
}
```

You will need to fill the following field (in quoted ""):
- senderPhoneNumber 
- TWILIO_AUTH_TOKEN
- TWILIO_ACCOUNT_SID

The message you want to send is in message.txt. 
- {firstname} correspond to the firstname of the victim
- {lastname} correspond to the lastname of the victim
- {uid} correspond to the Phishing Frenzy UID. You can use it like this: http://test.com/?uid={uid} in the SMS


Once the smishing.conf is filled, you will be introduced with the following menu:

`python3 smishing.py`

![Screenshot from 2020-05-04 12-08-30](https://user-images.githubusercontent.com/838845/80987415-01d37180-8e00-11ea-8625-0469249972c6.png)




## How to use phishingfrenzy.py

This script is just to convert the XML targets list from Phishing Frenzy to CSV format. Then, the Smishing script can import those targets.

`python3 phishingfrenzy.py`

```
usage: phishingfrenzy.py [-h] xml_file csv_file

positional arguments:
  xml_file    XML file from PhishingFrenzy that is usually called
              download_stats.xml.
  csv_file    Write to CSV file.

optional arguments:
  -h, --help  show this help message and exit
```


