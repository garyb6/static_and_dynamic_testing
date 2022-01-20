import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("spades", 9)
        self.card2 = Card("diamonds", 1)
        self.card3 = Card("hearts", 3)
        self.card4 = Card("clubs", 6)
        self.cards = [self.card3, self.card4]
        self.cardgame = CardGame 

    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self, self.card2))
    
    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardgame.highest_card(self, self.card1, self.card2))
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 9", self.cardgame.cards_total(self, self.cards))