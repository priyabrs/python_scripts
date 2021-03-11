import json
import requests
import pandas as pd

ENDPOINT_URL = "https://cricket-live-data.p.rapidapi.com/series"
HEADERS = {
    'x-rapidapi-host': "cricket-live-data.p.rapidapi.com",
    'x-rapidapi-key': "5a16df460dmsh2c16b9bddccc908p13510fjsn4ee3f19d9f0e"
    }

ID_SERIES_TYPE = {'Test':0, 'T20I':1, 'T20':2, 'ODI':3 , 'List A':4, 'First Class':5}
def load_series_data(file_name = 'series_data.json'):
    response = requests.request("GET", ENDPOINT_URL, headers=HEADERS)
    with open (file_name, 'w') as series_data:
        json.dump(response.json(), series_data)

def get_series_data_from_json(file_name = 'series_data.json'):
    with open (file_name, 'r') as series_data:
        json_data = json.load(series_data)
    return json_data

def get_fixtures_by_series(series_id): 
    url = "https://cricket-live-data.p.rapidapi.com/fixtures-by-series/"+series_id
    response = requests.request("GET", url, headers=HEADERS)
    return response.json()

def get_match_by_fixture(fixture_id):
    url = "https://cricket-live-data.p.rapidapi.com/match/"+fixture_id
    response = requests.request("GET", url, headers=HEADERS)
    return response.json()
    
def get_series_dataframe_by_type(series_type):
    series_json_data = get_series_data_from_json()
    series_data_list = series_json_data['results'][ID_SERIES_TYPE[series_type]]['series']
    series_dataframe = pd.DataFrame(series_data_list)
    return series_dataframe 

def get_match_ids(series_id):
    match_id_list = []
    fixture_json = get_fixtures_by_series(series_id)
    for fixture_dict in fixture_json['results']:
        match_id_list.append(fixture_dict['id'])
    return match_id_list

if __name__ == '__main__':
    # get_series_data()
    # with open ('series_data.json', 'r') as series_data:
    #     json_data = json.load(series_data)    
    # df = get_series_dataframe_by_type('T20')
    # cond1 = df['series_name'] == 'Indian Premier League'  
    # cond2 = df['season'] == '2021'
    # print(df[cond1 & cond2].series_id.iloc[1])
    json_data = get_fixtures_by_series('833')
    # json_data = get_match_by_fixture('2508221')
    # with open ('fixture_data.json', 'w') as series_data:
    #     json.dump(json_data, series_data)
    match_list = get_match_ids('833')
    print(match_list)
    # print(json_data)