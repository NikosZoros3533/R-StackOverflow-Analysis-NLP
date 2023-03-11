import time
import pandas as pd
from stackapi import StackAPI
import csv
import json
import random
import os.path


idsofowners112 = {993414, 9790769, 17590417, 5970296, 19794621, 3867094, 3428818, 3949312, 4401242, 15271002,
               3944959, 2870897, 4803875, 15133880, 8755535, 9049980, 14839865, 12567016, 5560493, 10920547,
               5005410, 8889021, 18214471, 18336226, 19621105, 2802810, 2962003, 9458151, 20388122, 11394263,
               4757814, 5057296, 19262443, 7845734, 17106269, 8464159, 15905836, 8995064, 9285876, 4941290,
               5103995, 12456821, 12047641, 7293631, 11437322, 15553518, 5958680, 6057032, 2784067, 8111143,
               11388629, 9630669, 12282058, 1497338, 15986327, 2865290, 1798908, 10419473, 7228144, 11878576,
               8102861, 1272594, 9008223, 15856464, 13550516, 13870373, 7507568, 2596602, 4054643, 5251742,
               10530140, 892071, 12478649, 12326087, 8966221, 17907602, 8667256, 14874374, 17448770, 20371419,
               4322048, 3886279, 6378990, 19676936, 13400539, 180219, 12213672, 2356119, 1898986, 10739838,
               13604719, 6312563, 804253, 3540724, 697964, 5142360, 4975144, 3541045, 1438908, 4343562, 10998057, 11766396,
               7474569, 11953784, 2030296, 13342467, 13122297, 5775436, 7441389, 4203273, 4982995, 965145}
idsofowners10 = {10530140, 892071, 12478649, 12326087, 8966221, 17907602, 8667256, 14874374, 17448770, 20371419}

SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 100
SITE.max_pages = 100




def extract_questions_of_users(dataa):
    questionsdict = []

    for item in dataa["items"]:
        ownerid = 0
        ownerdisplay = 0
        if 'owner' in item:
            ownerid = item['owner'].get('user_id')
            ownerdisplay = item['owner'].get('display_name')
        tempquestion = {
            'tags': item['tags'],
            'is_answered': item['is_answered'],
            'view_count': item['view_count'],
            'down_vote_count': item['down_vote_count'],
            'up_vote_count': item['up_vote_count'],
            'answer_count': item['answer_count'],
            'score': item['score'],
            'last_activity_date': item['last_activity_date'],
            'creation_date': item['creation_date'],
            'question_id': item['question_id'],
            'link': item['link'],
            'title': item['title'],
            'body': item['body'],
            'owner_user_id': ownerid,
            'owner_display_name': ownerdisplay,

        }
        questionsdict.append(tempquestion)
    return questionsdict


def remove_fetched_ids_from_all(file, ids):
    with open(file) as f:
        usersids = set(json.load(f))

    usersids.difference_update(ids)
    with open(file, 'w') as f:
        json.dump(list(usersids), f)


def fetch_questions_by_ids(temp_ids):
    customfilter = '!*MjkmySTGk)eZ2O6'
    batch_data = SITE.fetch('users/{ids}/questions', ids=temp_ids, filter=customfilter)


    return batch_data


def save_in_csv_file(file, questions):
    if os.path.exists(file):
        dataframe1 = pd.DataFrame.from_records(questions)
        dataframe1.to_csv(file, mode='a', index=False, header=False)

    else:
        dataframe1 = pd.DataFrame.from_records(questions)
        dataframe1.to_csv(file, mode='w', index=False)








def fetch_all_questions_by_ids(ids):
    questions = []

    while ids:
        batch = random.sample(list(ids), min(10, len(ids)))

        data = fetch_questions_by_ids(set(batch))
        tempquestions = extract_questions_of_users(data)
        save_in_csv_file("questionsbyonwers.csv", tempquestions)
        questions.extend(tempquestions)

        ids -= set(batch)
        remove_fetched_ids_from_all("idsofowners100.json", batch)
    return questions


#  tempquestionsdata = fetch_questions_by_ids(idsofowners10)
questions2 = fetch_all_questions_by_ids(idsofowners112)
print(questions2)
print(len(questions2))




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



#read ids from json
            with open("idsofowners100.json") as f:
            usersids = set(json.load(f))



 # Remove processed user IDs from input file
        users.difference_update(user_ids)
        data['items'] = list(users)
        with open(input_file, 'w') as f:
            json.dump(data, f)
            
            
            
values = random.sample(list(idsofowners100), 10)
idsofowners100 -= set(values)





# Open the JSON file
with open("example.json", "r") as file:
    data = json.load(file)

# Convert the list of strings to a list of integers
items = [int(item) for item in data["items"]]

# Write the list of integers to a new file
with open("output.json", "w") as file:
    json.dump(items, file)
"""