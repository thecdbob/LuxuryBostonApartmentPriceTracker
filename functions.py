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
from pymongo import MongoClient

EpochTimeInt = int(time.time())
EpochTimeString = str(EpochTimeInt)
dayinseconds = 86400

def epoch_to_date(epoch_time):
    return datetime.datetime.utcfromtimestamp(epoch_time).strftime('%m/%d/%Y')

#interates through current data to two weeks beyond
for i in range(14):
    print(epoch_to_date(EpochTimeInt + dayinseconds*i))