"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime   
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def getCallsByMonthYear(phoneCall, month, year):

    timestamp = phoneCall[2]
    dt = datetime.strptime(timestamp, '%d/%m/%Y %H:%M')
    if(dt.year == year and dt.month == month):
        return True
    else:
        return False

def trackCallDuration(dictionary, phoneNumber, callDuration):
    if(dictionary.get(phoneNumber) == None):
        dictionary[phoneNumber] = dictionary.get(phoneNumber,0) + int(callDuration)
    else:
        dictionary[phoneNumber] = int(dictionary.get(phoneNumber)) + int(callDuration)
    return dictionary

records = filter(lambda x: getCallsByMonthYear(x, 9, 2016), calls)

dictionary = {}
for record in records:
    timestamp = record[2]
    callDuration = record[3]

    dictionary = trackCallDuration(dictionary, record[0], record[3])
    dictionary = trackCallDuration(dictionary, record[1], record[3])

phoneMax = max(dictionary.items(), key=lambda x: int(x[1]))

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phoneMax[0],phoneMax[1]))
