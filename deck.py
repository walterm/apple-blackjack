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
        self.refreshDeck()

    def refreshDeck(self):
        self.cards = []
        for rank in Deck.ranks:
            for suit in Deck.suits:
                if rank == '1':
                    self.cards.append('10'+suit)
                else: self.cards.append(rank+suit)
        Deck.shuffle(self)
    
    def shuffle(self):
        shuffle(self.cards)

    def drawCard(self):
        if len(self.cards) == 0:
            raise RuntimeError("Deck is empty!")
        return self.cards.pop(0)
        
         

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def testInit(self):
        self.assertEqual(len(self.deck.cards), 52)

    def testDrawCard(self):
        card = self.deck.drawCard()
        self.assertEqual(len(self.deck.cards), 51)
        self.assertEqual(card in self.deck.cards, False)
        for i in range(51):
            self.deck.drawCard()
        self.assertRaises(RuntimeError, self.deck.drawCard)
        try:
            self.deck.drawCard()
        except RuntimeError:
            self.deck.refreshDeck()
        self.assertEqual(len(self.deck.cards), 52)        

if __name__ == '__main__':
    unittest.main()

        
