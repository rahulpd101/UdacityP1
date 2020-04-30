"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoingCallsList = set()
recievingCallslist = set()

telemarketersCallslist = set()

for record in calls:
    outgoingNumber = record[0]
    recievingNumber = record[1]

    if outgoingNumber not in outgoingCallsList:
        outgoingCallsList.add(outgoingNumber)

    if recievingNumber not in recievingCallslist:
        recievingCallslist.add(recievingNumber)


outgoingTextsList = set()
recievingTextslist = set()
for record in texts:
    outgoingNumber = record[0]
    recievingNumber = record[1]

    if outgoingNumber not in outgoingTextsList:
        outgoingTextsList.add(outgoingNumber)

    if recievingNumber not in recievingTextslist:
        recievingTextslist.add(recievingNumber)

for phoneNum in outgoingCallsList:
    if((phoneNum not in recievingCallslist) and (phoneNum not in outgoingTextsList) and (phoneNum not in recievingTextslist)):
        telemarketersCallslist.add(phoneNum)


print("These numbers could be telemarketers: ")
print(*sorted(telemarketersCallslist), sep='\n')
