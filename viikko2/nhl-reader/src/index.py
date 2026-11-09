from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player import PlayerReader, PlayerStats

SEASONS = [
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
]

NATIONALITIES = [
    "USA",
    "FIN",
    "CAN",
    "SWE",
    "CZE",
    "RUS",
    "SLO",
    "FRA",
    "GBR",
    "SVK",
    "DEN",
    "NED",
    "AUT",
    "BLR",
    "GER",
    "SUI",
    "NOR",
    "UZB",
    "LAT",
    "AUS",
]


def main():
    console = Console()
    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")
    nationality = Prompt.ask("Nationality", choices=NATIONALITIES, default="FIN")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = make_table(season, nationality, players)
    console.print(table)


def make_table(season, nationality, players):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Name")
    table.add_column("Team")
    table.add_column("Points")

    for player in players:
        points = f"{player.goals} + {player.assists} = {player.goals + player.assists}"
        table.add_row(player.name, player.team, points)

    return table


if __name__ == "__main__":
    main()
