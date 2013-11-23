from random import shuffle
import unittest
class Deck:
    heart = u'\u2661'.encode('utf-8')
    diamond = u'\u2662'.encode('utf-8')
    spade = u'\u2660'.encode('utf-8')
    club = u'\u2663'.encode('utf-8')
    suits = [heart, diamond, spade, club]
    ranks = '234567891JQKA'
    def __init__(self):
        self.cards = []
        for rank in Deck.ranks:
            for suit in Deck.suits:
                if rank == '1':
                    self.cards.append('10'+suit)
                else: self.cards.append(rank+suit)
        Deck.shuffle(self)

    def shuffle(deck):
        shuffle(deck.cards)
         

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertEqual(len(self.deck.cards), 52)

if __name__ == '__main__':
    unittest.main()

        
