import requests


class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.nationality = dict["nationality"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players = []
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = filter(lambda x: x.nationality == nationality, players)
        sorted_players = sorted(
            filtered_players, key=lambda x: x.goals + x.assists, reverse=True
        )

        return sorted_players
