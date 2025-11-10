from rich import print as rprint
from rich.table import Table
from rich.prompt import Prompt
from statistics_service import PlayerReader, PlayerStats

def select_season():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    season = Prompt.ask("Season ", choices=seasons, default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    return PlayerStats(reader), season

def select_nationality(stats):
    nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]
    nationality = Prompt.ask("Nationality ", choices=nationalities, default="", case_sensitive=False)
    return stats.top_scorers_by_nationality(nationality), nationality

def fancy_print(players, season, nationality):
    stats_table = Table(
        "Name",
        "Team(s)",
        "Goals",
        "Assists",
        "Points",
        title=f"Season {season} players from {nationality}",
    )

    for player in sorted(players, key=lambda player: player.points, reverse=True):
        stats_table.add_row(f"[blue]{player.name}", f"[magenta]{player.team}", f"[green]{player.goals}", f"[green]{player.assists}", f"[green]{player.points}")

    print()
    rprint(stats_table)
    print()

def main():
    print()
    seasonal_stats, season = select_season()
    while True:
        players, nationality = select_nationality(seasonal_stats)
        fancy_print(players, season, nationality)

if __name__ == "__main__":
    main()
