import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89),  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_top_scorer(self):
        top_scorers = self.stats.top(1)
        self.assertEqual(top_scorers[0].name, "Gretzky")

    def test_top_goals(self):
        top_goals = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_goals[0].name, "Lemieux")

    def test_top_assists(self):
        top_assists = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_assists[0].name, "Gretzky")

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.goals, 4)

    def test_searched_player_does_not_exist(self):
        player = self.stats.search("Selänne")
        self.assertEqual(player, None)

    def test_team(self):
        team = self.stats.team("PIT")
        self.assertEqual(team[0].name, "Lemieux")
