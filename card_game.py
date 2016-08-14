class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        card = self.rank + self.suit
        return card
card1 = Card("A","d")
print(card1)

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            reply = " "
            for card in self.cards:
                reply += str(card) + " "
        else:
            reply = "<empty>"

        return reply

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self,card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
other_hand = Hand()
my_hand = Hand()
my_hand.add(card1)
my_hand.give(card1,other_hand)
print(other_hand)
print(my_hand)

print(my_hand)
print(other_hand)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 0):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards")

deck1 = Deck()
print(deck1)
deck1.populate()
print(deck1)
deck1.shuffle()
print(deck1)
deck1.shuffle()
print(deck1)
Player_hand = Hand()
Dealer_hand = Hand()
hands = [Player_hand, Dealer_hand]
deck1.shuffle()
deck1.deal(hands,per_hand=2)
print(deck1)
deck1.deal(hands,per_hand=1)
print(Player_hand)
print(Dealer_hand)






