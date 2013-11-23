
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

d = Deck()
        
