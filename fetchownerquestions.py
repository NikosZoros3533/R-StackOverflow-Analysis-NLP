import time
import pandas as pd
from stackapi import StackAPI
import csv
import json

idsofowners={993414, 9790769, 17590417, 5970296, 19794621, 3867094, 3428818, 3949312, 4401242, 15271002,
             3944959, 2870897, 4803875, 15133880, 8755535, 9049980, 14839865, 12567016, 5560493, 10920547,
             5005410, 8889021, 18214471, 18336226, 19621105, 2802810, 2962003, 9458151, 20388122, 11394263,
             4757814, 5057296, 19262443, 7845734, 17106269, 8464159, 15905836, 8995064, 9285876, 4941290,
             5103995, 12456821, 12047641, 7293631, 11437322, 15553518, 5958680, 6057032, 2784067, 8111143,
             11388629, 9630669, 12282058, 1497338, 15986327, 2865290, 1798908, 10419473, 7228144, 11878576,
             8102861, 1272594, 9008223, 15856464, 13550516, 13870373, 7507568, 2596602, 4054643, 5251742,
             10530140, 892071, 12478649, 12326087, 8966221, 17907602, 8667256, 14874374, 17448770, 20371419,
             4322048, 3886279, 6378990, 19676936, 13400539, 180219, 12213672, 2356119, 1898986, 10739838,
             13604719, 6312563, 804253, 3540724, 697964, 5142360, 4975144, 3541045, 1438908, 4343562}
idsofowners2 = {993414, 9790769, 17590417, 5970296, 19794621, 3867094, 3428818, 3949312, 4401242, 15271002}

SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 100
SITE.max_pages = 100


data = SITE.fetch('users/{ids}/questions', ids=idsofowners , filter='!*MjkmySTGk)eZ2O6')
print(data)



"""
SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 10
SITE.max_pages = 1

SITE.fetch('users/{ids}/questions', ids=idsofowners.pop(100), filter="withbody")




put ids in a json file
        with open('questionstagRwithoutdupls4.csv', 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            idsofowners = {row['owner_user_id'] for row in reader}

        print(len(idsofowners))

        ids={'items': list(idsofowners)}
        with open('idsofowners.json', 'w') as f:
            json.dump(ids, f)



"""