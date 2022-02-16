from unicodedata import name


class League():
    def __init__(self, league_id, league_name, league_type, country, seasons, teams=[]) -> None:
        self.league_id = league_id
        self.league_name = league_name
        self.league_type = league_type
        self.country = country
        self.seasons = seasons
        self.teams = teams

    
    # @classmethod
    # def find_by_name(cls, league_name) -> int:
    #     if cls.league_name == league_name:
    #         return cls.league_id
