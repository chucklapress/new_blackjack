import random

class Card(object):

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        deck = []
        for card in self.cards:
            deck.append(str(card))
        return '\n'.join(deck)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)


deck = Deck()
print(deck)
card1 =Card(2, 1)
print(card1)

class Hand:
    def __init__(self, label=''):
        self.cards = Card(3,5)
        self.label = label


    def add_card(self):
        pass


hand1 = Hand('Player')
hand2 = Hand('Dealer')
print(hand1.cards)
print(hand1.label)
print(hand2.label)







