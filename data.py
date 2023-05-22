# import requests library
import requests

# make api call

result = requests.get('https://opentdb.com/api.php?amount=10&category=17&type=boolean')

# replace result from api to question data

question_data = result.json()['results']
