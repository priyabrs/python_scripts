
from types import CoroutineType
from unicodedata import name


class Team():
    def __init__(self, team_id, league_id, name, country, founded, venue_name, venue_address, venue_city, venue_capacity) -> None:
        self.team_id = team_id
        self.league_id = league_id
        self.name = name
        self.country = country
        self.founded = founded
        self.venue_name = venue_name
        self.venue_address = venue_address
        self.venue_city = venue_city
        self.venue_capacity = venue_capacity