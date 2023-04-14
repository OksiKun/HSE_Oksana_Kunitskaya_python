# 1
# a)

import json
import csv
import re

data_txt = []
with open("traders.txt") as file:
    for line in file:
        data_txt.append([x for x in line.split()])
for i in range(len(data_txt)):
    data_txt[i] = data_txt[i][0]

# b), с)

with open("traders.json") as f:
    data_json = json.load(f)

listCSV = []

for j in range(len(data_txt)):
    INN = data_txt[j]
    for i in range(len(data_json)):
        if "inn" in data_json[i] and INN == data_json[i]['inn']:
            listCSV.append({'INN': INN, 'OGRN': data_json[i]["ogrn"], 'Address': data_json[i]["address"]})
            break


with open('traders.csv', 'w', newline='') as csvFile:
    wr = csv.DictWriter(csvFile, delimiter = ';', fieldnames = ['INN', 'OGRN', 'Address'])
    wr.writeheader()
    for i in listCSV:
        wr.writerow(i)

# 2

def searchMails(text):
    lst = re.findall('\S+@\S+', text)
    return lst

with open('1000_efrsb_messages.json') as file:
    data_jsonMails = json.load(file)

dictMails = {}

for i in range(len(data_jsonMails)):
    listMails = set(searchMails(data_jsonMails[i]['msg_text']))
    if listMails != set():
        dictMails[str(data_jsonMails[i]['publisher_inn'])] = listMails

with open('emails.json', 'w') as outfile:
    json.dump(dictMails, outfile, default=list)
