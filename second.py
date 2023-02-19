
from stackapi import StackAPI
import json
"""
idskeys = (3325952, 21098497, 18169859, 7898115, 7489539, 14348302,
           14612502, 186904, 21027866, 19726876, 5133853, 3632673, 21197349,
           21193770, 21185588, 10260021, 1969717, 4463161, 3056186, 1958465, 19621442,
           21195331, 9610309, 851530, 8507470, 2583119, 2855510, 5961303, 13574232, 21194330,
           11968604, 9575517, 21186653, 5209697, 7205986, 4560996, 21197418, 19873387, 16620147, 14367863,
           20544120, 3018873, 4396154, 1145978, 21195391, 21194368, 697473, 18727041, 8926337, 21099653, 21118088,
           21195402, 21167244, 21196944, 8128145, 973458, 21147285, 4285081, 9489566, 4561056, 20929701, 16433830, 14482089,
           20146350, 8689326, 366256, 18880691, 9203380, 21186752, 20899009, 21195458, 17661126, 10084551, 12284109, 18090706,
           21193427, 21174489, 8547033, 17935579, 20548828, 15509724, 13414621, 21190367, 12356835, 21194468,
           14924529, 14764277, 2781431, 21166332, 18830589, 7192318, 15274239, 21195010, 21107973, 13406982, 19393798,
           11932936, 17446666, 21193483, 1306892, 21196047, 3361552, 17799953, 21151000, 9323801, 10924836, 16185637, 5235494,
           6447399, 20266285, 20206895, 8250673, 12896561, 21194548, 12308789, 75062, 21094712, 487229, 18364222, 7033156, 21199688,
           21199177, 14483273, 2530121, 21194576, 21097810, 12914005, 21183318, 21197143, 20307801, 10107738, 2782564,
           17098600, 7965040, 8622453, 17447797, 10407800, 11883900, 13529981, 19404669, 21190017, 16567173, 21193605,
           20557703, 19342733, 17163664, 10796433, 21198236, 12941731, 4052900, 21194149, 12977063, 15813037, 11340206,
           7871409, 19167156, 21192631, 1894845, 17275326, 20761536, 15420355, 9877445, 20877255, 10771401, 21198282,
           21195210, 2055626, 18251213, 2319308, 15013328, 3584466, 8279507, 18136532, 7703513, 19325405, 17288160,
           20785124, 7996904, 21153261, 2245102, 20947953, 20701170, 14767090, 14994425, 21196794, 18255867, 8673278
)

idkeys10set = (3325952, 21098497, 18169859, 7898115, 7489539, 14348302,
            14612502, 186904, 21027866, 19726876,)
idkeys2 = [3325952, 21098497]
idkeys10 = list(idkeys10set)

# idkeyslist = list(idskeys)



SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 100
SITE.max_pages = 100







with open('example.json') as json_f:
    data = json.load(json_f)

print(data["items"][0]["owner"])







with open('questionsR.json') as json_f:
    data = json.load(json_f)


questionsbyusers = SITE.fetch('users/{ids}/questions', ids=21098497)


           questionofowner = {
               'is_answered': item['is_answered'],
               'view_count': item['view_count'],
               'closed_date': item['closed_date'],
               'answer_count': item['answer_count'],
               'score': item['score'],
               'last_activity_date': item['last_activity_date'],
               'creation_date': item['creation_date'],
               'last_edit_date': item['last_edit_date'],
               'question_id': item['question_id'],
               'link': item['link'],
               'closed_reason': item['closed_reason'],
               'title': item['title'],
               'body': item['body'],
                           }





SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 100
SITE.max_pages = 1
customfilter = '!*MjkmySTGk)eZ2O6'
data = SITE.fetch('questions', filter=customfilter, include='votes', tagged='R')











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




questions = extract_question(data)
print(questions)

