import random

'''
Spades → 3
Hearts → 2
Diamonds → 1
Clubs → 0
'''
class Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __repr__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)


    def shuffle(self):
        random.shuffle(self.cards)


    def sort(self):
        self.cards.sort()


    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __repr__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return self.label + '\n' + '\n'.join(res) + '\n'+ '\n'



'''
c1 = Card(1, 12)
c2 = Card(3,2)
print((c1, c2))
print(c1 < c2)

deck = Deck()
# print(deck)
hand = Hand('first_hand')
# card = deck.pop_card()
# hand.add_card(card)
# print(hand)

# deck.move_cards(hand, 5)
# print(hand)
# print()
# print()
# hand.shuffle()
# print(hand)
# print()
# print()
# hand.sort()
# print(hand)

print(deck.deal_hands(4,13))

'''


