import random
import itertools

suits = {"C":0,"D":0,"H":0,"S":0}
ranks = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10,"A":1}


deck = tuple(''.join(card) for card in itertools.product(ranks,suits))
hand = random.sample(deck, 2)

value = sum(ranks[card[0]] + suits[card[1]] for card in hand)


print("Player hand:", str(hand))
print("Value:", str(value))