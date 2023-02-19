import requests
from stackapi import StackAPI
import json
import time



"""
TODO

-->dump in a jsonfile
rquestions = SITE.fetch('questions', tagged='R',page=....)
use data dump


-->Collect the question history of the users(ids) that asked with the tag R 
iterate into ids and create a dict with info of owner one time and all his questions  


"""





idskeys = set()







"""
This function take data as a parameter and extract a list of dictionaries that are made in
the function ,that each question is formatted as
"title":title
"body":body
"""
def extract_question(dataa):
    questionsdict = []
    for item in dataa["items"]:
        accepted_answer_id = 0
        if "accepted_answer_id" in item:
            accepted_answer_id = item['accepted_answer_id']
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
            'owner_user_id': item["owner"]['user_id'],
            'owner_display_name': item["owner"]['display_name']

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
    global idskeys

    for item in data["items"]:
        user = item["owner"]
        idkey = item["owner"]["user_id"]
        if idkey not in idskeys:
            unique_users.append(user)
        idskeys.add(idkey)

    return unique_users







"""This function fetch all  questions and returns them ,as well as all the unique owners of these"""
def fetch_all_data():
    startpage = 1
    fetching = True
    questions = []
    owners = []

    while fetching:
        data = fetch_batch_questions(startpage)
        print("fetching...")
        owners.extend(extract_unique_users(data))
        questions.extend(data["items"])
        has_more = data["has_more"]
        backoff = data["backoff"]
        quota_remaining = data["quota_remaining"]
        if not has_more or len(questions) >= 480000:
            return questions, owners
        if quota_remaining <= 3:
            time.sleep(3600)
            print("sleeping for the day")
        if backoff:
            time.sleep(backoff+1)
            print("sleeping for a sec")
        time.sleep(1)
        startpage += 100
    return questions, owners




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
        if not has_more or len(questions) >= 200:
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













SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 10
SITE.max_pages = 10








questions_wth_tag_R, owners_of_questions = testing_fetch_all_data()
print(questions_wth_tag_R)
print(len(questions_wth_tag_R))
# print(questions_wth_tag_R)
# print(owners_of_questions)


















"""
with open("questionsR.json", "w") as f:
    json.dump(questionsR, f)


with open('questionswithbody.json') as json_f:
    questions4 = json.load(json_f)

print(len(questionsR))
print(len(ownersofR))

"""



"""
with open("questions.json", "w") as f:
    json.dump(questions, f)
"""





