import base64
import time
import uuid
import json
from random import choices
from string import ascii_uppercase, ascii_lowercase, digits
import requests
import logging

logging.basicConfig(filename='logging.log', level=logging.DEBUG)
logging.info('Running through program')

population = ascii_uppercase + ascii_lowercase + digits
def char_gen(n):
    return str.join('', choices(population, k=n))

token = base64.b64encode(str.encode(char_gen(1) + '236070A81C6067EA630B5920B65E2A22' + char_gen(3) + 'A0909810A6D132832E28EF6DA18EC77C' + char_gen(5) + base64.b64encode(str.encode(str(int(time.time() * 1000)))).decode() + char_gen(7))).decode()
#print(token)

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

response = requests.get('https://leasing.realpage.com/RP.Leasing.AppService.WebHost/workflowstartup/v1/4527024/', params=params, headers=headers)

if response.status_code == 200:
    # convert the response to json
    json_data = response.json()

    # format the json data

    # used for initially creating the code
    #print(json.dumps(json_data, indent=4))

    # variables for to get names for pricing

    Timestamp = str(int(time.time() * 1000))

    # add i to the variable because it won't work right now
    Floorplans = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][0]['Floorplans']
    #Name = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][0]['Name']
    #Id = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][0]['Id']
    #UnitIds = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][0]['UnitIds']
    #Descriptions = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][0]['Description']

    # count number of elements in the json data for 'FloorPlans'
    FloorPlanLength = len(json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][0]['Floorplans'])
    #print(FloorPlanLength)

    #create a list that stores objects of the class FloorPlan
    #create an object of the class FloorPlan
    #store the name, description, bedrooms, bathrooms, squarefeet, minpricerange, maxpricerange in the object

    FloorPlanList = []

    siteid = '4527024' #not sure if this changes or not (pmalden)
    selectedunitid = siteid

    #for testing purposes
    #print(siteid)
    #  we need to pass in, unit id, selectedunitsiteid, and floorplan id
    for i in range(FloorPlanLength):
        #if multiple units parse all of them
        for j in range(len(Floorplans[i]['UnitIds'])):
            FloorPlan = {
                'Name': Floorplans[i]['Name'],
                'ID' : Floorplans[i]['Id'],
                'UnitID': Floorplans[i]['UnitIds'][j],
                'TimeStamp': Timestamp,
            }
            FloorPlanList.append(FloorPlan)

    #for i in range(len(FloorPlanList)):
        #print(FloorPlanList[i])
        #print('\n')

    #pass in objects to find pricing next

    #create list of objects to use for each unit's price
    #UnitPriceList = []

    for FloorPlan in FloorPlanList:
        json_data = {
            'NavigationMode': 2,
            'ActivityID': '5e38bcd1-df47-4e97-b807-ff6d90f4d64a',
            'IsSkipStep': False,
            'PmcId': '2507719',
            'SiteId': siteid,
            'LeasingIntent': 'SearchUnit',
            'AppStateParams': {
                'FloorplanId': '8597091',
                'MoveInDate': '07/31/2022', #change to dynamic date
                'UnitId': FloorPlan['UnitID'],
                'SelectedUnitSiteId': selectedunitid,
            },
        }
        print(FloorPlanList[2])

        response1 = requests.put('https://leasing.realpage.com/RP.Leasing.AppService.WebHost/appstate/v1/', params=params, headers=headers, json=json_data)

        if response1.status_code == 200:
            # convert the response to json
            json_data = response1.json()

            #try catch (needs to be fixed in the future)
            try:
                MonthlyCostLength = len(json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][2]['UnitDetails']['PricePlans'])
                MonthlyCostDict = {}
                print('break1')
                for i in range(MonthlyCostLength):
                    Months = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][2]['UnitDetails'][
                            'PricePlans'][i]['DurationInMonths']
                    Cost = json_data['Workflow']['ActivityGroups'][0]['GroupActivities'][2]['UnitDetails']['PricePlans'][
                            i]['MonthlyRent']
                    MonthlyCostDict.update({Months: Cost})
                print('break2')
                FloorPlanList[i].append(MonthlyCostDict)
                print('added data to' + FloorPlanList[i]['Name'])

            except:
                print('break')
                #delete unit if unable to find pricing
                logging.error('Move in Date invalid ' + FloorPlan['UnitID'])


            logging.info('Updated prices for Floor Plan List')
            print('Updated prices for Floor Plan List')
            print(FloorPlanList[1])

        else:
            logging.error('Non 200 response in response1')

elif response.status_code == 401:
        logging.error('401 error')

else:
    logging.error('Not 401 or 200 response')