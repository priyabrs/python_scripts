# import requests
# from env import api_key

# url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

# querystring = {"id":"39"}

# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': api_key.API_KEY
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.json())

# import requests
# import json
# from dataload import LEAGUE_DF, LEAGUE_OBJ_DICT
# import requests

# url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': api_key.API_KEY
#     }

# response = requests.request("GET", url, headers=headers)

# with open ('league_details.json', 'w') as file:
#     json.dump(response.json(), file)
# print(response.json())
# print(LEAGUE_OBJ_DICT)

# import pandas as pd
# df = pd.DataFrame({'gender':list('MMMFFF'),
#                    'height':[4,5,4,5,5,4],
#                    'age':[70,80,90,40,2,3]})

# # print (df)
# column = ['height', 'age', 'gender']
# equal = ['>', '>', '==']
# condition = [1.68, 20, 'F']
# query = ' & '.join(f'{i} {j} {repr(k)}' for i, j, k in zip(column, equal, condition))
# print(df.query(query))