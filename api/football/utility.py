from dataload import league_data_load, team_data_load, DataLoadException
import time
import datetime

def get_league_obj_by_team_param(**kwargs):
    team_id_list = team_data_load.get_team_id_by_parameter(**kwargs)
    if len(team_id_list) < 1:
        raise DataLoadException('Team id not present for provided parameters')
    if len(team_id_list) > 1:
        raise DataLoadException('Multiple teams with same parameters. Please provide more filters')
    else:
        team_id = team_id_list[0]
        league_id = int(team_data_load.get_team_by_id(team_id).league_id)
        league_obj = league_data_load.get_league_by_id(league_id)
    return league_obj

# league_obj = get_league_obj_by_team_param(name = 'FC Barcelona')
# print(league_obj.league_name)
# league_ids = league_data_load.get_league_id_by_parameter(country = 'Italy')
# for id in league_ids:
#     league_obj = league_data_load.get_league_by_id(id)
#     print(id, league_obj.league_name)
# id = league_data_load.get_league_id_by_parameter(league_name = 'premier')
# print(id)
# league_obj_dict = league_data_load.get_league_obj_dict()
# print(league_obj_dict[179])






# def get_league_by_id(league_id) -> object:
#     '''
#     Returns a league object for the league id
#     '''
#     return league_data_load.league_obj_dict[league_id]
#     # return LEAGUE_OBJ_DICT[league_id]

# def get_team_by_id(team_id):
#     return team_data_load.team_obj_dict[team_id]

# def get_league_df_by_parameter(**kwargs):
#     join_str = ''
#     if len(kwargs) > 1:
#         join_str = ' & '
#     query_str = join_str.join([f'{k} == {repr(v)}' for k, v in kwargs.items()])
#     return league_data_load.league_df.query(query_str)

# def get_league_id_by_parameter(**kwargs):
#     league_df = get_league_df_by_parameter(**kwargs)
#     return league_df.league_id.values

# # league_list = []
# # nation_list = ['Belgium','France','Brazil','England','Portugal','Spain','Argentina','Uruguay','Mexico','Italy','Croatia','Denmark','Germany','Netherlands','Colombia','Switzerland','Chile','Wales','Poland','Sweden','USA','Austria','Ukraine','Japan','Turkey','Russia','Hungary','Australia','Ireland','Czech-Republic','Norway','Scotland']
# # for nation in nation_list:
# #     df = get_df_by_parameter(country = nation, league_type = 'League')
# #     league_list.append(df.sort_values('league_id').league_id.values[0])
# # # get_id_by_parameter(league_name='Premier League')
# # print(league_list)
# # obj = find_by_league_id(144)

# obj = get_team_by_id(1428)
# print(obj.name)