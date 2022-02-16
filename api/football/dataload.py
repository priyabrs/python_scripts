import json
from urllib import response
import pandas as pd
from league import League
from team import Team
import requests
import time
import config
from env import api_key

class DataLoadException(Exception):
    pass

class DataLoad():
    endpoint_url = "https://api-football-v1.p.rapidapi.com/v3/"
    headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': api_key.API_KEY
            }

    def __init__(self, nations, leagues) -> None:
        self.nations = nations
        self.leagues = leagues
        
    def load_data_from_api(self, json_file = None, suffix = None, url = None):
        if suffix and url:
            raise DataLoadException("The function can only have 'suffix' or 'url', not both as arguments")
        elif suffix:
            url = self.endpoint_url+suffix
        response = requests.request("GET", url, headers=self.headers)
        if json_file:
            with open (json_file, 'w') as file:
                json.dump(response.json(), file)
        else:
            return response.json()
    
    def get_obj_df_by_parameter(self, dataframe, **kwargs):
        join_str = ''
        if len(kwargs) > 1:
            join_str = ' & '
        query_str = join_str.join([f'{k} == {repr(v)}' for k, v in kwargs.items()])
        return dataframe.query(query_str)


class LeagueData(DataLoad):

    league_json_file = './data/league_details.json'

    def __init__(self, nations, leagues) -> None:
        super().__init__(nations, leagues)
        self.league_data_list = self.load_league_data_from_json()
        self.league_df = pd.DataFrame(self.league_data_list)
        self.league_obj_dict = {league_dict['league_id']:League(league_dict['league_id'], league_dict['league_name'], league_dict['league_type'], league_dict['country'], league_dict['seasons']) for league_dict in self.league_data_list}

    def load_league_data_from_json(self):
        league_data_list = []    
        with open(self.league_json_file , 'r') as league_data_file:
            league_data_json = json.load(league_data_file)
        for data_dict in league_data_json['response']:
            league_data_dict = {}
            league_data_dict['league_id'] = data_dict['league']['id']
            league_data_dict['league_name'] = data_dict['league']['name']
            league_data_dict['league_type'] = data_dict['league']['type']
            league_data_dict['country'] = data_dict['country']['name']
            league_data_dict['seasons'] = [season_dict['year'] for season_dict in data_dict['seasons']]
            league_data_list.append(league_data_dict)
        return league_data_list

    def get_league_by_id(self,league_id) -> object:
        '''
        Returns a league object for the league id
        '''
        return self.league_obj_dict[league_id]

    def get_league_id_by_parameter(self, **kwargs):
        filtered_league_df = self.get_obj_df_by_parameter(self.league_df, **kwargs)
        return filtered_league_df.league_id.values

    def reload_league_data(self):
        self.load_data_from_api(json_file=self.league_json_file, suffix='leagues')
        #TODO
        self.__init__(config.nations, config.league_ids)

    def get_league_obj_dict(self):
        return self.league_obj_dict

class TeamData(DataLoad):

    team_json_file = './data/team_details.json'
    team_v2_json_file = './data/team_v2_data.json'

    def __init__(self, nations, leagues) -> None:
        super().__init__(nations, leagues)
        self.league_team_map = self.load_team_v2_data_from_json()
        self.team_data_list = self.create_team_data_list()
        self.team_df = pd.DataFrame(self.team_data_list)
        self.team_obj_dict = {team_dict['team_id']:Team(team_dict['team_id'], team_dict['league_id'], team_dict['name'], team_dict['country'], team_dict['founded'], team_dict['venue_name'], team_dict['venue_address'], team_dict['venue_city'], team_dict['venue_capacity']) for team_dict in self.team_data_list}

    def create_team_data_list(self):
        team_data_list = []
        for league_id, team_list in self.league_team_map.items():
            for team_dict in team_list:
                team_dict['league_id'] = league_id
                team_data_list.append(team_dict)
        return team_data_list

    def load_team_v2_data_from_json(self): 
        with open(self.team_v2_json_file , 'r') as team_data_file:
            league_data_json = json.load(team_data_file)
        team_data_list = [data_dict for data_dict in league_data_json['league_team_map'].values()]
        return league_data_json['league_team_map']
    
    def get_team_by_id(self, team_id):
        return self.team_obj_dict[team_id]

    def get_team_id_by_parameter(self, **kwargs):
        filtered_team_df = self.get_obj_df_by_parameter(self.team_df, **kwargs)
        return filtered_team_df.team_id.values

    def reload_team_data_by_league(self):
        league_team_map = {}
        for league_id in config.league_ids:
            time.sleep(4)
            v2_url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/"+str(league_id)
            response_json = self.load_data_from_api(url=v2_url)
            league_team_map[league_id] = response_json['api']['teams']
        with open (self.team_v2_json_file, 'w') as v2_file:
            json.dump({'league_team_map':league_team_map}, v2_file)


league_data_load = LeagueData(config.nations, config.league_ids)
team_data_load = TeamData(config.nations, config.league_ids)

# print(team_data_load.team_obj_dict[144])
# team_data_list = team_data_load.load_team_v2_data_from_json()
# print([team_dict for team_dict in team_data_load.team_data_list[0]])

# for team_list in team_data_load.team_data_list:
#     for team_dict in team_list:
#         print(team_dict)

# print([team_dict for team_list in team_data_load.team_data_list for team_dict in team_list])
# print(team_data_load.get_team_by_id(1428).name)
# print(league_data_load.get_league_id_by_parameter(league_name = 'Random'))
# print(team_data_load.get_team_id_by_parameter(name = 'CSKA 1948'))
# print(team_data_load.team_df)
# print(league_data_load.league_df.columns)