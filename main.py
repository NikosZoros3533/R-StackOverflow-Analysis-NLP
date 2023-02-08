import requests
from stackapi import StackAPI
import json

SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")


"""
TODO
-->make a function that start from startpage  (with pagesize  100) and go up till maxpagesize=100
and collect 10000 questions.

-->call that function until the property "hasmore"=false 

-->dump in a jsonfile
rquestions = SITE.fetch('questions', tagged='R',page=....)
"""
SITE.page_size = 100
SITE.max_pages = 100
rquestions = SITE.fetch('questions', tagged='R',)

with open("rrquestions.json", "w") as f:
    json.dump(rquestions, f)


print(len(rquestions['items']))



