from stackapi import StackAPI
import json


SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 10
SITE.max_pages = 1


questionsbyusers = SITE.fetch('users/{ids}/questions', ids=[4288660, 19120757])
print(questionsbyusers)



