class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict["nationality"]
        self.assists = player_dict["assists"]
        self.goals = player_dict["goals"]
        self.points = self.assists + self.goals
        self.team = player_dict["team"]

    def __str__(self):
        return f"{self.name:25} {self.team:20} {self.goals:2} + {self.assists:2} = {self.points}"
