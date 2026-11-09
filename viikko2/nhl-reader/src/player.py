import requests


class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.nationality = data["nationality"]
        self.team = data["team"]
        self.goals = data["goals"]
        self.assists = data["assists"]

    def __str__(self):
        points = f"{self.goals} + {self.assists} = {self.goals + self.assists}"
        return f"{self.name:20} {self.team:15} {points}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players = []
        response = requests.get(self.url, timeout=10).json()
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
