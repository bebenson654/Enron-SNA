import json
from pprint import pprint

# ------------------------------------------------------------------------------
# Reads in the out.json from the extractor. Outputs a new json with just a sender and list of recipent for each email
# ------------------------------------------------------------------------------

with open('./out.json', 'r') as f:
    emails = json.load(f)

folders = emails.keys()

# The senders dictionary will be used to overritw the sender for each email from a users "sent_items" folder to the same sender
senders = {}

finalJson = {}

for folder in folders:
    senders[folder] = []
    tmp = []

    for email in emails[folder].keys():
        tmp.append(emails[folder][email]['From'])

        ID = folder + ': ' +email
        finalJson[ID] = {}
        
        finalJson[ID]['Sender'] = emails[folder][email]['From']

        finalJson[ID]['Recipients'] = []
        for t in emails[folder][email]['To']:
            if '@enron.com' in t and t not in finalJson[ID]['Recipients']:
                finalJson[ID]['Recipients'].append(t)

        for c in emails[folder][email]['Cc']:
            if '@enron.com' in c and c not in finalJson[ID]['Recipients']:
                finalJson[ID]['Recipients'].append(c)

        for b in emails[folder][email]['Bcc']:
            if '@enron.com' in b and b not in finalJson[ID]['Recipients']:
                finalJson[ID]['Recipients'].append(b)

    # counts the number of times each address appears as the sender for each user
    tmp2=[]
    for t in tmp:
        if t not in tmp2:
            c = tmp.count(t)
            senders[folder].append((t,c))
        tmp2.append(t)



newSenders = {}
for s in senders:
    if senders[s]:
        newSenders[s] = {}
        myList = senders[s]
        myList.sort(reverse=True, key=lambda a: a[1])

        newSenders[s]['Address'] = myList[0][0]
        newSenders[s]['Overwrite'] = []
        for m in myList[1:]:
            newSenders[s]['Overwrite'].append(m[0])


for email in finalJson:
    folder = email.split(': ')[0]
    if finalJson[email]['Sender'] in newSenders[folder]['Overwrite']:
        finalJson[email]['Sender'] = newSenders[folder]['Address']

    rec = finalJson[email]['Recipients']
    if rec:
        for i in range(len(rec)):
            if rec[i] in newSenders[folder]['Overwrite']:
                rec[i] = newSenders[folder]['Address']

# removes any emails with no sender or recipients
tmp = []
for f in finalJson:
    if finalJson[f]['Sender'] == '' or finalJson[f]['Recipients'] == []:
        tmp.append(f)

for t in tmp:
    del finalJson[t]


# writes the dictionary to a JSON file
with open('./final.json', 'w') as outFile:
    json.dump(finalJson, outFile)