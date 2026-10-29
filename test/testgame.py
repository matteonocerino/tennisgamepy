import unittest

from src.errors import GameHasAlreadyBeenWonError, DuplicatedPlayerError
from src.game import Game

class TestGame(unittest.TestCase):

    def test_love_forty(self):
        game = Game("Sinner", "Alcaraz")
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        status = game.get_game_status()
        self.assertEqual("Sinner love - Alcaraz forty", status)

    def test_forty_thirty(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        status = game.get_game_status()
        self.assertEqual("Sinner forty - Alcaraz thirty", status)

    def test_fifteen_love(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        game.increment_player_score(player_name_1)
        status = game.get_game_status()
        self.assertEqual("Sinner fifteen - Alcaraz love", status)

    def test_thirty_fifteen(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_2)
        status = game.get_game_status()
        self.assertEqual("Sinner thirty - Alcaraz fifteen", status)

    def test_player1_wins(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        status = game.get_game_status()
        self.assertEqual("Sinner wins", status)

    def test_player2_wins(self):
        game = Game("Sinner", "Alcaraz")
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        status = game.get_game_status()
        self.assertEqual("Alcaraz wins", status)

    def test_deuce(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        status = game.get_game_status()
        self.assertEqual("Deuce", status)

    def test_advantage_player1(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_1)
        status = game.get_game_status()
        self.assertEqual("Advantage Sinner", status)

    def test_advantage_player2(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        player_name_2 = game.get_player2_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        game.increment_player_score(player_name_2)
        status = game.get_game_status()
        self.assertEqual("Advantage Alcaraz", status)

    def test_Game_Has_Already_Been_Won_Error(self):
        game = Game("Sinner", "Alcaraz")
        player_name_1 = game.get_player1_name()
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        game.increment_player_score(player_name_1)
        self.assertRaises(GameHasAlreadyBeenWonError, game.increment_player_score, player_name_1)

    def test_duplicate_name_error(self):
        self.assertRaises(DuplicatedPlayerError, Game, "Sinner", "Sinner")