import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []
    nationality = "FIN"

    for player_dict in response:
        if player_dict["nationality"] == nationality:
            player = Player(player_dict)
            players.append(player)

    print(f"Players from {nationality}:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
