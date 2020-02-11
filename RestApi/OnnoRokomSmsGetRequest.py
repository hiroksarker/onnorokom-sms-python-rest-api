#OnnoRokom SMS Website For Registration - https://onnorokomsms.com
import requests

# BASE URL
URL = 'https://api2.onnorokomsms.com/HttpSendSms.ashx'
#All Options Params
op              = 'OneToMany' #Request Method (Change as your requirement)
username        = '' #Username
password        = '' #Password
smsText         = '' #SMS Text
mobile          = '' #Recipient Mobile Number (Single and Multiple Number Support (Comma Sperated) )
type            = 'TEXT' #SMS Type
maskName        = ''
campaignName    = ''

# data to be sent to api
PARAMS = {
    'op'            : op,
    'username'      : username,
    'password'      : password.encode(),
    'smsText'       : smsText.encode(),
    'mobile'        : mobile,
    'type'          : type,
    'maskName'      : maskName,
    'campaignName'  : campaignName
}
# sending get request and saving response
res = requests.get(url = URL, params=PARAMS)
data = res.text
# Response Print
print("SMS Response: ", data)

