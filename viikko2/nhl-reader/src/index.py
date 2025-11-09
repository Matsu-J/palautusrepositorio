from statistics_service import PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in sorted(players, key=lambda player: player.points, reverse=True):
        print(player)

if __name__ == "__main__":
    main()
