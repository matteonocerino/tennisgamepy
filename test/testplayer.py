import unittest

from src.player import Player


class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        # Arrange
        player = Player("Sinner")
        # Act
        name = player.get_name()
        #Asert
        self.assertEqual("Sinner", name)  # add assertion here

    def test_set_name(self):
        # Arrange
        player = Player("Sinner")
        # Act
        player.set_name("Alcaraz")
        # Asert
        name = player.get_name()
        self.assertEqual("Alcaraz", name)  # add assertion here

    def test_get_score(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        score = player.get_score()
        #Asert
        self.assertEqual(3, score)  # add assertion here

    def test_set_score(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        player.set_score(5)
        # Assert
        score = player.get_score()
        self.assertEqual(5, score)

    def test_increment_score(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        player.increment_score()
        # Assert
        score = player.get_score()
        self.assertEqual(4, score)

    def test_get_0_as_string(self):
        # Arrange
        player = Player("Sinner")
        # Act
        score_as_str = player.get_score_as_string()
        # Assert
        self.assertEqual("love", score_as_str)

    def test_get_1_as_string(self):
        # Arrange
        player = Player("Sinner", 1)
        # Act
        score_as_str = player.get_score_as_string()
        # Assert
        self.assertEqual("fifteen", score_as_str)

    def test_get_2_as_string(self):
        # Arrange
        player = Player("Sinner", 2)
        # Act
        score_as_str = player.get_score_as_string()
        # Assert
        self.assertEqual("thirty", score_as_str)

    def test_get_3_as_string(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        score_as_str = player.get_score_as_string()
        # Assert
        self.assertEqual("forty", score_as_str)

    def test_get_4_as_string(self):
        # Arrange
        player = Player("Sinner", 4)
        # Act
        score_as_str = player.get_score_as_string()
        # Assert
        self.assertIsNone(score_as_str)

    def test_is_tied_with(self):
        # Arrange
        player1 = Player("Sinner", 4)
        player2 = Player("Alcaraz", 4)
        # Act
        tie = player1.is_tied_with(player2)
        # Assert
        self.assertTrue(tie)

    def test_is_not_tied_with_p1_advantage(self):
        # Arrange
        player1 = Player("Sinner", 5)
        player2 = Player("Alcaraz", 4)
        # Act
        tie = player1.is_tied_with(player2)
        # Assert
        self.assertFalse(tie)

    def test_is_not_tied_with_p2_advantage(self):
        # Arrange
        player1 = Player("Sinner", 4)
        player2 = Player("Alcaraz", 5)
        # Act
        tie = player1.is_tied_with(player2)
        # Assert
        self.assertFalse(tie)

    def test_has_at_least_forty_points(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        forty_points = player.has_at_least_forty_points()
        # Assert
        self.assertTrue(forty_points)

    def test_does_not_have_at_least_forty_points(self):
        # Arrange
        player = Player("Sinner", 2)
        # Act
        forty_points = player.has_at_least_forty_points()
        # Assert
        self.assertFalse(forty_points)

    def test_has_less_than_forty_points(self):
        # Arrange
        player = Player("Sinner", 2)
        # Act
        outcome = player.has_less_than_forty_points()
        # Assert
        self.assertTrue(outcome)

    def test_does_not_have_less_than_forty_points(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        outcome = player.has_less_than_forty_points()
        # Assert
        self.assertFalse(outcome)

    def test_has_more_than_forty_points(self):
        # Arrange
        player = Player("Sinner", 4)
        # Act
        outcome = player.has_more_than_forty_points()
        # Assert
        self.assertTrue(outcome)

    def test_does_not_have_more_than_forty_points(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        outcome = player.has_more_than_forty_points()
        # Assert
        self.assertFalse(outcome)

    def test_has_one_point_advantage_on(self):
        # Arrange
        player1 = Player("Sinner", 4)
        player2 = Player("Alcaraz", 3)
        # Act
        outcome = player1.has_one_point_advantage_on(player2)
        # Assert
        self.assertTrue(outcome)

    def test_does_not_have_one_point_advantage_on_equal_score(self):
        # Arrange
        player1 = Player("Sinner", 3)
        player2 = Player("Alcaraz", 3)
        # Act
        outcome = player1.has_one_point_advantage_on(player2)
        # Assert
        self.assertFalse(outcome)

    def test_does_not_have_one_point_advantage_on_p2_advantage(self):
        # Arrange
        player1 = Player("Sinner", 3)
        player2 = Player("Alcaraz", 4)
        # Act
        outcome = player1.has_one_point_advantage_on(player2)
        # Assert
        self.assertFalse(outcome)

    def test_has_at_least_two_points_advantage_on(self):
        # Arrange
        player1 = Player("Sinner", 5)
        player2 = Player("Alcaraz", 3)
        # Act
        outcome = player1.has_at_least_two_points_advantage_on(player2)
        # Assert
        self.assertTrue(outcome)

    def test_does_not_have_at_least_two_points_advantage_on_one_point_advantage(self):
        # Arrange
        player1 = Player("Sinner", 4)
        player2 = Player("Alcaraz", 3)
        # Act
        outcome = player1.has_at_least_two_points_advantage_on(player2)
        # Assert
        self.assertFalse(outcome)

    def test_does_not_have_at_least_two_points_advantage_on_equal_score(self):
        # Arrange
        player1 = Player("Sinner", 3)
        player2 = Player("Alcaraz", 3)
        # Act
        outcome = player1.has_at_least_two_points_advantage_on(player2)
        # Assert
        self.assertFalse(outcome)

    def test_does_not_have_at_least_two_points_advantage_on_p2_advantage(self):
        # Arrange
        player1 = Player("Sinner", 3)
        player2 = Player("Alcaraz", 5)
        # Act
        outcome = player1.has_at_least_two_points_advantage_on(player2)
        # Assert
        self.assertFalse(outcome)