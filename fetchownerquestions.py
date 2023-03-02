import time
import pandas as pd
from stackapi import StackAPI
import csv




with open('questionstagRwithoutdupls4.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    idsofowners = {row['owners_id'] for row in reader}


SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 10
SITE.max_pages = 1

SITE.fetch('users/{ids}/questions', ids=idsofowners.pop(100), filter="withbody")


