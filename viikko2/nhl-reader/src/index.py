from statistics_service import PlayerReader, PlayerStats
<<<<<<< HEAD
from rich import print as rprint
from rich.table import Table, Column

def main():
    print()
    
    while True:
        rprint(f"Season [magenta][2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25] [blue](2024-25)\n[white]Enter 0 to quit")
        season = input()
        seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
        if season == "0":
            return
        elif season == "":
            season = "2024-25"
        if str(season) in seasons:
            url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
            reader = PlayerReader(url)
            stats = PlayerStats(reader)
            break
        else:
            print("No information found")
            continue
    
    while True:
        rprint("Nationality [magenta][USA, FIN, CAN, SWE, CZE, RUS, SLO, FRA, GBR, SVK, DEN, NED, AUT, BLR, GER, SUI, NOR, UZB, LAT, AUS]\n[white]Enter 0 to quit")
        nationality = input()
        nationality = nationality.upper()
        if nationality == "0":
            return
        try:
            players = stats.top_scorers_by_nationality(nationality)
            if len(players) <= 0:
                print("No information found")
                continue
        except:
            print("No information found")
            continue
        
        print()
        stats_table = Table(
            "Name",
            "Team(s)",
            "Goals",
            "Assists",
            "Points",
            title=f"Season {season} players from {nationality}",
        )

        for player in sorted(players, key=lambda player: player.points, reverse=True):
            stats_table.add_row(f"[blue]{player.name}", 
                                f"[magenta]{player.team}", 
                                f"[green]{player.goals}", 
                                f"[green]{player.assists}", 
                                f"[green]{player.points}")
        
        rprint(stats_table)
        print()
=======

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in sorted(players, key=lambda player: player.points, reverse=True):
        print(player)
>>>>>>> 0eaa6b36f5b18c17090505065c3da38f8b5dfe27

if __name__ == "__main__":
    main()
