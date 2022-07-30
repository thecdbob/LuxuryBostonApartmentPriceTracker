import time
import datetime
import base64
import uuid
import json
from random import choices
from string import ascii_uppercase, ascii_lowercase, digits
import requests
import logging
import pymongo
import sys


'''
logging section of functions
'''
logging.basicConfig(level=logging.DEBUG, handlers=[
    logging.FileHandler('logging.log'),
    logging.StreamHandler(sys.stdout)
])
'''
end of logging section of functions
'''


'''
time section of functions
'''

EpochTimeInt = int(time.time())
EpochTimeString = str(EpochTimeInt)
dayinseconds = 86400

# convert epoch time to date month year in the format of mm/dd/yyyy
def epoch_to_date(epoch_time):
    return datetime.datetime.utcfromtimestamp(epoch_time).strftime('%m/%d/%Y')

# to be used in future to generate data for units with different move in date
# interates through current data to two weeks beyond
# for i in range(14):
    # print(epoch_to_date(EpochTimeInt + dayinseconds*i))
'''
end of time section of functions
'''



'''
Authentication section for oceans and jmalden
'''
population = ascii_uppercase + ascii_lowercase + digits
def char_gen(n):
    return str.join('', choices(population, k=n))

token = base64.b64encode(str.encode(char_gen(1) + '236070A81C6067EA630B5920B65E2A22' + char_gen(3) +
                                    'A0909810A6D132832E28EF6DA18EC77C' + char_gen(5) +
                                    base64.b64encode(str.encode(str(int(time.time() * 1000)))).decode() +
                                    char_gen(7))).decode()
# print(token)

session_id = str(uuid.uuid4())
'''
end of Authentication section for oceans and jmalden
'''


'''
MongoDB section of functions
'''

# connetion info
client = pymongo.MongoClient\
    ("mongodb+srv://cdbob:xca8xbp9vxa.gnt1DZR@cluster0.yspvvbs.mongodb.net/?retryWrites=true&w=majority")
# database to write to
db = client.test
# for systems that use this particular style of booking system
collection = db.floorplans

'''
End of MongoDB section of functions
'''