import os
from pathlib import Path
import re
import json

# ------------------------------------------------------------------------------
# extracts to, from, cc, bcc, and subject from each users "sent_items" folder
# creates JSON with that info
# ------------------------------------------------------------------------------

usrDirs = os.listdir("./maildir")
users = {}

# iterate over list of folders
for d in usrDirs:
    users[d] = {} # create a nested dictionary for each folder
    path = Path(Path.cwd(), "maildir", d, "sent_items")

    # regex for capturing the "From", "To", and "Subject" of each email
    fromToSub = re.compile(r"From: (.*)\n(To: ([\s\S]*?))?Subject: (.*)")
    # regex for captuing the Cc or Bcc of each email
    CcBcc = re.compile(r"Cc: ([\s\S]*?)Mime[\s\S]*Bcc: ([\s\S]*?)X")

    if os.path.exists(path): # if the folder has a "sent_items" folder
        messages = os.listdir(path) # list of all emails in that folder

        for m in messages:
            users[d][m] = {} # creates nested dict for each email

            with open(Path(path, m)) as f:
                wholeFile = f.read()

                result = fromToSub.search(wholeFile)
                if result:
                    users[d][m]["From"] = result.group(1)

                    # splits "To" into a list of addresses and strips them
                    if result.group(3):
                        to = result.group(3).strip().split(', ')
                        for i in range(len(to)):
                            to[i] = to[i].strip()
                        users[d][m]["To"] = to
                    else:    
                        users[d][m]["To"] = []
                    
                    users[d][m]["Subject"] = result.group(4)


                users[d][m]["Cc"] = []
                users[d][m]["Bcc"] = []
                result = CcBcc.search(wholeFile)

                if result:
                    Cc = result.group(1).strip()
                    Bcc = result.group(2).strip()

                    # removes values from Bcc that are also in CC
                    if Cc == Bcc:
                        Bcc = []
                    else:
                        Bcc = Bcc.split(', ')

                    Cc = Cc.split(', ')

                    for i in range(len(Cc)):
                        Cc[i] = Cc[i].strip()
                        if Cc[i] in Bcc:
                            Bcc.remove(Cc[i])

                    users[d][m]["Cc"] = Cc
                    users[d][m]["Bcc"] = Bcc

# removes user's that have no "sent_items"
empty = []
for u in users:
    if users[u] == {}:
        empty.append(u)
for  e in empty:
    del users[e]


# writes the dictionary to a json file
with open('./out.json', 'w') as outFile:
    json.dump(users, outFile)