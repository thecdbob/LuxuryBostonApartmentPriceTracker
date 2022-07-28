import base64
import time
import uuid
import json
from random import choices
from string import ascii_uppercase, ascii_lowercase, digits

'''
A03.1 - 1 Bed/1 Bath
'''

population = ascii_uppercase + ascii_lowercase + digits
def char_gen(n):
    return str.join('', choices(population, k=n))

token = base64.b64encode(str.encode(char_gen(1) + '236070A81C6067EA630B5920B65E2A22' + char_gen(3) + 'A0909810A6D132832E28EF6DA18EC77C' + char_gen(5) + base64.b64encode(str.encode(str(int(time.time() * 1000)))).decode() + char_gen(7))).decode()
#print(token)

import requests

session_id = str(uuid.uuid4())

headers = {
    'authority': 'leasing.realpage.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'origin': 'https://7744255.onlineleasing.realpage.com',
    'referer': 'https://7744255.onlineleasing.realpage.com/',
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

json_data = {
    'NavigationMode': 2,
    'ActivityID': '5e38bcd1-df47-4e97-b807-ff6d90f4d64a',
    'IsSkipStep': False,
    'PmcId': '2507719',
    'SiteId': '4527024',
    'LeasingIntent': 'SearchUnit',
    'AppStateParams': {
        'FloorplanId': '8597091',
        'MoveInDate': '07/29/2022',
        'UnitId': '121',
        'SelectedUnitSiteId': '4527024',
    },
}

response = requests.put('https://leasing.realpage.com/RP.Leasing.AppService.WebHost/appstate/v1/', params=params, headers=headers, json=json_data)
'''
if response.status_code == 200:
    # convert the response to json
    json_data = response.json()

    # format the json data

    # used for initially creating the code
    #print(json.dumps(json_data, indent=4))

    # count number of elements in the json data for 'FloorPlans'
    MonthlyCostLength = len(json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][2]['UnitDetails']['PricePlans'])
    #print(MonthlyCostLength)

    # take the name, despcription, bedrooms, bathrooms, squarefeet, minpricerange, maxpricerange from each floor plan
    # create a list that stores objects of the class FloorPlan
    # store the name, description, bedrooms, bathrooms, squarefeet, minpricerange, maxpricerange in the object
    # print the object

    #create a list that stores objects of the class FloorPlan
    #create an object of the class FloorPlan
    #store the name, description, bedrooms, bathrooms, squarefeet, minpricerange, maxpricerange in the object

    MonthlyCostList = []
    for i in range(MonthlyCostLength):
        MonthlyCost = {
            'Cost': json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][2]['UnitDetails']['PricePlans'][i]['MonthlyRent'],
            'Months': json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][2]['UnitDetails']['PricePlans'][i]['DurationInMonths'],
            'TimeStamp': str(int(time.time() * 1000))
        }
        MonthlyCostList.append(MonthlyCost)

    # print objects from floorplanlist with 0 'Bedrooms' (studio)
    #for i in range(FloorPlanLength):
        #if FloorPlanList[i]['Bedrooms'] == 0:
            #print(FloorPlanList[i])

    # print objects from floorplanlist with 0 'Bedrooms' (studio)
    # print the name of the floorplan and the MaxPriceRange of the floorplan


    for i in range(MonthlyCostLength):
        print(MonthlyCostList[i]['Cost'])
        print(MonthlyCostList[i]['Months'])
        #print space between each floorplan
        print(' ')

elif response.status_code == 401:
    print('401 error')
else:
    print('Not 401 or 200 response')
'''
#"A05 - 1Bed/1Bath"

headers = {
    'authority': 'leasing.realpage.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://7744255.onlineleasing.realpage.com',
    'referer': 'https://7744255.onlineleasing.realpage.com/',
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
    'BpmId': 'OLL.LeaseTerms',
    'BpmSequence': '0',
    'LogSequence': '12',
    'ClientSessionID': session_id,
}

json_data = {
    'NavigationMode': 2,
    'ActivityID': '5e38bcd1-df47-4e97-b807-ff6d90f4d64a',
    'IsSkipStep': False,
    'PmcId': '2507719',
    'SiteId': '4527024',
    'LeasingIntent': 'SearchUnit',
    'AppStateParams': {
        'FloorplanId': '8597091',
        'MoveInDate': '07/29/2022',
        'UnitId': '121',
        'SelectedUnitSiteId': '4527024',
    },
}



response1 = requests.put('https://leasing.realpage.com/RP.Leasing.AppService.WebHost/appstate/v1/', params=params, headers=headers, json=json_data)
if response1.status_code == 200:
    # convert the response to json
    json_data = response.json()

    # used for initially creating the code
    print(json.dumps(json_data, indent=4))
else:
    print('uh oh')