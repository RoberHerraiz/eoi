import unittest


from cards import who_wins

# ToDo List:
# diferente cantidad de cartas -> raise error
#    ['1'],['3','4'] -> raise error
# cartas con invalidos,
#    'W' -> raise error
# case insensitive
#    ['j'],['J'] -> equivale a ['j'],['j']
# empate:
#    ['1'],['1'] -> "Tie"
# player1 wins y la puntuacion.
# player2 wins y la puntuacion.
# 2,3,4,5,6,7,8,9,10,J,Q,K,A/1


class CardsTests(unittest.TestCase):
    def test_numbers_of_cards_must_be_equal_for_both_players(self):
        self.assertRaises(ValueError, who_wins, ['1'], [])

    def test_there_must_be_at_least_one_card_per_player(self):
        self.assertRaises(ValueError, who_wins, [], [])

    def test_the_player_with_highest_cards_wins(self):
        self.assertEqual(who_wins(['5'], ['3']), "Player1 wins 1 to 0")
        self.assertEqual(who_wins(['2'], ['7']), "Player2 wins 1 to 0")

    def test_each_round_adds_up_one_point_to_the_players_score(self):
        self.assertEqual(who_wins(['5', '7'], ['3', '2']), "Player1 wins 2 to 0")

    def test_ace_is_the_highest_card_in_the_ranking(self):
        self.assertEqual(who_wins(['1'], ['10']), "Player1 wins 1 to 0")

    def test_a_game_may_end_up_with_a_tie(self):
        self.assertEqual(who_wins(['1'], ['1']), "Tie")
