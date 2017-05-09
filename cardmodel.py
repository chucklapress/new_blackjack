import random

class Card(object):

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None,'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank],
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

    def add_card(self):
        self.cards.append(self.cards)




deck = Deck()
deck.shuffle()


deck1 = deck.cards
for card in deck1:
    print(card)




class Hand:

    def __init__(self):
        self.cards = []


    def __str__(self):
        return str(self.cards)


    def draw(self, deck):
        card = deck.draw()
        self.cards.append(card)
        return card



class Player:
    def __init__(self):
        self.name = 'Player'
        self.hand = Hand()

    def __str__(self):
        return "{} has  ".format(self.name) + str(self.hand)


player1 = Player()
print(player1)


class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = Hand()

    def __str__(self):
        return "{} has  ".format(self.name) + str(self.hand)

house_dealer = Dealer()
print(house_dealer)
