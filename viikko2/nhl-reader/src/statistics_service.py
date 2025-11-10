import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url, timeout=60).json()

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player_dict in self.reader.response:
            if player_dict["nationality"] == nationality:
                player = Player(player_dict)
                players.append(player)
        return players
