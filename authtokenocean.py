#Adapted from code written by Razr
#for Ocean
import base64
import time
import uuid
from random import choices
from string import ascii_uppercase, ascii_lowercase, digits


population = ascii_uppercase + ascii_lowercase + digits
def char_gen(n):
    return str.join('', choices(population, k=n))

"""
 Formula: 
 
    1 random character + 32 characters + 3 random characters + 32 characters + 5 random characters
 
    1 random character + rpcalc(siteid ex 4527024) + 3 random characters +
    A0909810A6D132832E28EF6DA18EC77C (user agent rpcalc) + 5 random characters +
"""

token = base64.b64encode(str.encode(char_gen(1) + '5E77154BF5F07E77E5A5B65388A871CF' + char_gen(3) + '0909810A6D132832E28EF6DA18EC77Cf' + char_gen(5) + base64.b64encode(str.encode(str(int(time.time() * 1000)))).decode() + char_gen(7))).decode()
print(token)

import requests

session_id = str(uuid.uuid4())

headers = {
    'authority': 'leasing.realpage.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'origin': 'https://7796310.onlineleasing.realpage.com',
    'referer': 'https://7796310.onlineleasing.realpage.com',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'xyz': token,
}

params = {
    'BpmId': 'OLL.WorkflowStartUp',
    'BpmSequence': '0',
    'LogSequence': '3',
    'ClientSessionID': session_id,
}

response = requests.get('https://leasing.realpage.com/RP.Leasing.AppService.WebHost/workflowstartup/v1/4501693/', params=params, headers=headers)
print(response)