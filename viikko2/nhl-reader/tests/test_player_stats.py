import unittest
from src.player import Player, PlayerStats


class StubPlayerReader:
    """Stub PlayerReader that returns predefined test data without internet access."""

    def __init__(self, players_data):
        self.players_data = players_data

    def get_players(self):
        return [Player(data) for data in self.players_data]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        """Set up test data for each test."""
        self.test_data = [
            {
                "name": "Alex Ovechkin",
                "nationality": "Russia",
                "team": "Washington Capitals",
                "goals": 50,
                "assists": 30,
            },
            {
                "name": "Connor McDavid",
                "nationality": "Canada",
                "team": "Edmonton Oilers",
                "goals": 40,
                "assists": 60,
            },
            {
                "name": "Sidney Crosby",
                "nationality": "Canada",
                "team": "Pittsburgh Penguins",
                "goals": 35,
                "assists": 45,
            },
            {
                "name": "Evgeny Kuznetsov",
                "nationality": "Russia",
                "team": "Washington Capitals",
                "goals": 32,
                "assists": 50,
            },
            {
                "name": "Artemi Panarin",
                "nationality": "Russia",
                "team": "Edmonton Oilers",
                "goals": 38,
                "assists": 55,
            },
        ]
        self.reader = StubPlayerReader(self.test_data)
        self.stats = PlayerStats(self.reader)

    def test_top_scorers_by_nationality_canada(self):
        """Test filtering and sorting by Canadian nationality."""
        canadians = self.stats.top_scorers_by_nationality("Canada")

        self.assertEqual(len(canadians), 2)
        self.assertEqual(canadians[0].name, "Connor McDavid")  # 100 points total
        self.assertEqual(canadians[1].name, "Sidney Crosby")  # 80 points total

    def test_top_scorers_by_nationality_russia(self):
        """Test filtering and sorting by Russian nationality."""
        russians = self.stats.top_scorers_by_nationality("Russia")

        self.assertEqual(len(russians), 3)
        self.assertEqual(russians[0].name, "Artemi Panarin")  # 93 points total
        self.assertEqual(russians[1].name, "Evgeny Kuznetsov")  # 82 points total
        self.assertEqual(russians[2].name, "Alex Ovechkin")  # 80 points total

    def test_top_scorers_by_nationality_empty(self):
        """Test with nationality that doesn't exist."""
        result = self.stats.top_scorers_by_nationality("Sweden")

        self.assertEqual(len(result), 0)

    def test_top_scorers_by_team_washington(self):
        """Test filtering and sorting by Washington Capitals."""
        capitals = self.stats.top_scorers_by_team("Washington Capitals")

        self.assertEqual(len(capitals), 2)
        self.assertEqual(capitals[0].name, "Evgeny Kuznetsov")  # 82 points total
        self.assertEqual(capitals[1].name, "Alex Ovechkin")  # 80 points total

    def test_top_scorers_by_team_edmonton(self):
        """Test filtering and sorting by Edmonton Oilers."""
        oilers = self.stats.top_scorers_by_team("Edmonton Oilers")

        self.assertEqual(len(oilers), 2)
        self.assertEqual(oilers[0].name, "Connor McDavid")  # 100 points total
        self.assertEqual(oilers[1].name, "Artemi Panarin")  # 93 points total

    def test_top_scorers_by_team_empty(self):
        """Test with team that doesn't exist."""
        result = self.stats.top_scorers_by_team("Non-existent Team")

        self.assertEqual(len(result), 0)

    def test_top_scorers_by_team_single_player(self):
        """Test with team that has only one player."""
        penguins = self.stats.top_scorers_by_team("Pittsburgh Penguins")

        self.assertEqual(len(penguins), 1)
        self.assertEqual(penguins[0].name, "Sidney Crosby")

    def test_sorting_by_total_points(self):
        """Test that players are correctly sorted by total points."""
        canadians = self.stats.top_scorers_by_nationality("Canada")

        first_points = canadians[0].goals + canadians[0].assists
        second_points = canadians[1].goals + canadians[1].assists

        self.assertGreater(first_points, second_points)


if __name__ == "__main__":
    unittest.main()
