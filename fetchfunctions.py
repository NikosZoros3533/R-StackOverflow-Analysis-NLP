import time
import pandas as pd
from stackapi import StackAPI
import json
import csv

"""
TODO

-->dump in a jsonfile
rquestions = SITE.fetch('questions', tagged='R',page=....)
use data dump


-->Collect the question history of the users(ids) that asked with the tag R 
iterate into ids and create a dict with info of owner one time and all his questions  


"""





idsownerkeys = set()
questionids = set()








"""
This function take data as a parameter and extract a list of dictionaries that are made in
the function ,that each question is formatted as
"title":title
"body":body
"""
def extract_question(dataa):
    questionsdict = []
    global questionids
    for item in dataa["items"]:
        accepted_answer_id = 0
        ownerid = 0
        ownerdisplay = 0
        if "accepted_answer_id" in item:
            accepted_answer_id = item['accepted_answer_id']
        if 'owner' in item:
            ownerid = item['owner'].get('user_id')
            ownerdisplay = item['owner'].get('display_name')
        if item['question_id'] in questionids:
            continue
        questionids.add(item['question_id'])
        tempquestion = {
            'tags': item['tags'],
            'is_answered': item['is_answered'],
            'view_count': item['view_count'],
            'accepted_answer_id': accepted_answer_id,
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











"""
This function takes as parameter the page it should start and fetch the next maxpages x pagesize
questions and returns them
 """
def fetch_batch_questions(startpage):
    customfilter = '!*MjkmySTGk)eZ2O6'
    batch_of_questions = SITE.fetch('questions', filter=customfilter, include='votes', tagged='R', page=startpage)
    return batch_of_questions








"""
This takes as a parameter the data that we collect from the API and extact and return a list of unique users after it
saves their ids in the global set of ids 
"""
def extract_unique_users(data):
    unique_users = []
    global idsownerkeys

    for item in data["items"]:
        user = item["owner"]
        idkey = item["owner"]["user_id"]
        if idkey not in idsownerkeys:
            unique_users.append(user)
        idsownerkeys.add(idkey)

    return unique_users







"""This function fetch all  questions and returns them ,as well as all the unique owners of these"""
def fetch_all_data():
    startpage = 1
    has_more = True
    questions = []


    while has_more:
        data = fetch_batch_questions(startpage)
        print("fetching...")
        tempquestions = extract_question(data)
        questions.extend(tempquestions)
        has_more = data["has_more"]
        backoff = data["backoff"]
        quota_remaining = data["quota_remaining"]
        if len(questions) >= 20:
            print(f"checking...{has_more}")
            return questions
        if quota_remaining <= 3:
            time.sleep(3600)
            print("sleeping for the day")
        if backoff:
            time.sleep(backoff+1)
            print("backing off")
        print("sleeping for a sec")
        time.sleep(1)
        print(f"startpage:{startpage} and page:{data['page']}")
        startpage += 1





"""
This is the same as fetch_all_data function that is testing for a smaller 
amount of data
"""
def testing_fetch_all_data():
    startpage = 1
    fetching = True
    questions = []
    owners = []

    while fetching:
        data = fetch_batch_questions(startpage)
        print("fetching...")
        owners.extend(extract_unique_users(data))
        questions.extend(extract_question(data))
        has_more = data["has_more"]
        backoff = data["backoff"]
        quota_remaining = data["quota_remaining"]
        if not has_more or len(questions) >= 20:
            return questions, owners
        if quota_remaining <= 3:
            time.sleep(3600)
            print("sleeping for the day")
        if backoff:
            time.sleep(backoff+1)
            print("backing off")
        print("sleeping for a sec")
        time.sleep(1)
        startpage += 10
    return questions, owners


"""
This function takes the data as a parameter the ids of users that we want
to get all the questions from and return a list of dictionaries with the format
"owner":"owner_info"
"questions":"questions_info"
"""
def get_questions_by_users_id(ids):
    dictquestionsbyusers = []
    for key in ids:
        questions = []
        dataa = SITE.fetch('users/{ids}/questions', ids=key, filter="withbody")
        print(f"fetching the user with id {key}")
        for item in dataa["items"]:
            questionofowner = {}
            for dictkey in item:
                if (dictkey != "tags") and (dictkey != "owner"):
                    questionofowner[dictkey] = item[dictkey]

            questions.append(questionofowner)

        ownerandquestions = {"owner": dataa["items"][0]["owner"], "questions": questions}

        dictquestionsbyusers.append(ownerandquestions)
    return dictquestionsbyusers





def get_col_of_csv(csv_file, column):
    with open(csv_file, 'r', encoding='utf-8-sig') as file:  # 'questionstagRwithoutdupls4.csv'
        reader = csv.DictReader(file)
        columndata = [row[column] for row in reader]    # 'question_id'
    return columndata


def get_rid_of_dupls(csv_file):
    df = pd.read_csv(csv_file)
    df.drop_duplicates(subset=['question_id'], inplace=True)    # based on question id
    df.to_csv('questionstagRwithoutdupls4.csv', index=False)



SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 10
SITE.max_pages = 1


























"""

dataframe1 = pd.DataFrame.from_records(quetions_with_tag_R)
dataframe1.to_csv('questions_with_tagR.csv', index=False)



with open("questionsR.json", "w") as f:
    json.dump(questionsR, f)


with open('questionswithbody.json') as json_f:
    questions4 = json.load(json_f)

print(len(questionsR))
print(len(ownersofR))
  dataframe1 = pd.DataFrame.from_records(questions)
    dataframe1.to_csv('questions.csv', mode='w', index=False)





with open("questions.json", "w") as f:
    json.dump(questions, f)
    
    
    
setquestionsids = set(questionids)
print(len(setquestionsids))
print(len(questionids))


with open('questionstagRwithoutdupls4.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    questionids = [row['question_id'] for row in reader]










SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 100
SITE.max_pages = 100

fetch_all_data()





df = pd.read_csv('questionstagR.csv')
df.drop_duplicates(subset=['question_id'], inplace=True)
df.to_csv('questionstagRwithoutdupls2.csv', index=False)



dataframe1 = pd.DataFrame.from_records(questionsR)
dataframe1.to_csv('questions.csv', mode='w', index=False)



def extract_question(dataa):
    questionsdict = []
    global questionids
    for item in dataa["items"]:
        accepted_answer_id = 0
        ownerid = 0
        ownerdisplay = 0
        if "accepted_answer_id" in item:
            accepted_answer_id = item['accepted_answer_id']
        if 'owner' in item:
            ownerid = item['owner'].get('user_id')
            ownerdisplay = item['owner'].get('display_name')
        if item['question_id'] in questionids:
            continue
        questionids.add(item['question_id'])
        tempquestion = {
            'tags': item['tags'],
            'is_answered': item['is_answered'],
            'view_count': item['view_count'],
            'accepted_answer_id': accepted_answer_id,
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







def fetch_batch_questions(startpage):
    customfilter = '!*MjkmySTGk)eZ2O6'
    batch_of_questions = SITE.fetch('questions', filter=customfilter, include='votes', tagged='R', page=startpage)
    return batch_of_questions




def fetch_all_data():
    startpage = 500
    has_more = True



    while has_more:
        data = fetch_batch_questions(startpage)
        print("fetching...")
        questions = extract_question(data)
        dataframe1 = pd.DataFrame.from_records(questions)
        dataframe1.to_csv('questionstagRwithoutdupls3.csv', mode='a', index=False, header=False)

        has_more = data["has_more"]

        backoff = data["backoff"]
        quota_remaining = data["quota_remaining"]
        print(f"has more:{has_more},backoff:{backoff},quota_remaining{quota_remaining}")
        if quota_remaining <= 3:
            time.sleep(3600)
            print("sleeping for the day")
        if backoff:
            time.sleep(backoff+1)
            print("backing off")
        print("sleeping for a sec")
        time.sleep(1)
        print(f"startpage:{startpage} and page:{data['page']}")
        startpage += 100



"""





















