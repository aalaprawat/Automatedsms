
import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
numbers=["+917000090737","+919877470121","+919131352453",
            "+917389379177","+919542690689","+917000593119","+917000626163","+918921365708",""]
msg=" in numbers :

    response = sendPostRequest(URL, '1INAA3LCOKF7NXDGB4NSA7URIF12QBAW', 'BN17SVTZZGTGKXWL', 'prod/stage', i, 'active-sender-id', msg )
    