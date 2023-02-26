import time
import pandas as pd
from stackapi import StackAPI
import csv



idsownerkeys = set()




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



with open('questionstagRwithoutdupls4.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    questionids = [row['question_id'] for row in reader]

setquestionsids = set(questionids)


print(len(setquestionsids))
print(len(questionids))


"""








df = pd.read_csv('questionstagRwithoutdupls.csv')
df.drop_duplicates(subset=['question_id'], inplace=True)
df.to_csv('questionstagRwithoutdupls4.csv', index=False)






SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 100
SITE.max_pages = 100

fetch_all_data()


















df = pd.read_csv('questionstagR.csv')
df.drop_duplicates(subset=['question_id'], inplace=True)
df.to_csv('questionstagRwithoutdupls2.csv', index=False)



dataframe1 = pd.DataFrame.from_records(questionsR)
dataframe1.to_csv('questions.csv', mode='w', index=False)



"""

