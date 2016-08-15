import random


class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit

    def __str__(self):
        card = self.rank + self.suit
        return card


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            card_object = " "
            for card in self.cards:
                card_object += str(card) + " "
        else:
            card_object = "empty"

        return card_object

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)


    def give(self,card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def create(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 0):
        for cards in range(per_hand):
            for hand in hands:
                    top_card = self.cards[0]
                    self.give(top_card, hand)

    def hit(self, hand):
        top_card = self.cards[0]
        self.give(top_card, hand)



deck = Deck()
deck.create()
deck.shuffle()
deck1 = deck

print(deck1)
Player_hand = Hand()
Dealer_hand = Hand()
hands = [Player_hand, Dealer_hand]
deck1.deal(hands,per_hand=2)

print(deck1)


class Player:
    def __init__(self):
        self.name = "Player"
        self.hand = Player_hand

    def __str__(self):
        return "{} has  ".format(self.name) + str(self.hand)

print(Player())

class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.hand = Dealer_hand

    def __str__(self):
        return "{} has  ".format(self.name) + str(self.hand)

print(Dealer())




















