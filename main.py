import requests
from stackapi import StackAPI
import json

SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 4800
SITE.max_pages = 100
rquestions = SITE.fetch('questions', tagged='R')
#print(len(rquestions['items']))
#print(rquestions)
