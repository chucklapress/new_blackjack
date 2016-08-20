import random
import itertools

suits = "CHSD"
ranks = "A23456789TJQK"

Card = tuple(''.join(card) for card in itertools.product(ranks,suits))
Value = {card:min(1 + ranks.index(card[0]),10 )for card in Card }

class Deck:
    def __init__(self):
        self.cards = random.sample(Card, len(Card))

    def draw(self):
        if self.cards:
            return self.cards.pop()

class Hand:
    def __init__(self, deck):
        self.cards = []
        for card in range(2):
            self.draw(deck)

    def __str__(self):
        return ' '.join(self.cards)

    def draw(self, deck):
        card = deck.draw()
        self.cards.append(card)
        return card
def Game():

    deck = Deck()
    player = Hand(deck)
    dealer = Hand(deck)
    print("Dealer shows: {}".format(dealer.cards[0]))

    if True:
        print("Your hand: {}".format(player))
    else:
        pass

    choice = int(input("Type (1) to hold or (2) to hit "))
    if choice == 1 :
        pass
    elif choice == 2 :
        card = player.draw(deck)
        print("You drew: {}".format(player))
    if True:
        print("Dealer's hand: {}".format(dealer))
    else:
        pass


Game()


