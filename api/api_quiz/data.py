import requests

param = { 'amount': 10, 'type' : 'boolean'}
web_response = requests.get(url='https://opentdb.com/api.php', params=param)
web_response.raise_for_status()
data = web_response.json()
# print(data)
question_data = data["results"]
# print(question_data)
