import requests
from stackapi import StackAPI
import json

SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
rquestions = SITE.fetch('questions', tagged='R')
print(len(rquestions['items']))
print(rquestions)
