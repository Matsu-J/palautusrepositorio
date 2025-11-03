import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result.name, "Kurri")
        self.assertEqual(result.team, "EDM")
        self.assertEqual(result.goals, 37)
        self.assertEqual(result.assists, 53)
        self.assertEqual(result.points, 37+53)
    
    def test_search_non_existing(self):
        result = self.stats.search("Example")
        self.assertEqual(result, None)

    def test_find_existing_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(result[0].name, "Semenko")
        self.assertEqual(result[1].name, "Kurri")
        self.assertEqual(result[2].name, "Gretzky")
    
    def test_find_non_existing_team(self):
        result = self.stats.team("Example")
        self.assertEqual(len(result), 0)

    def test_best_player(self):
        top_player = self.stats.top(0)
        self.assertEqual(top_player[0].name, "Gretzky")
    
    def test_top_negative(self):
        top_player = self.stats.top(-1)
        self.assertEqual(len(top_player), 0)
        top_player = self.stats.top(-10)
        self.assertEqual(len(top_player), 0)
    
