
from __future__ import print_function, division

from Card import Hand, Deck
import pandas as pd


class PokerHand(Hand):

    poker_hands = { 1: 'pair', 2: 'two_pairs' , 3:'three' , 4: 'straight' , 5: 'flush' ,6: 'full_house' ,7: 'four', 8: 'straight_flush'}

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hist()
        for c in self.ranks.values():
            if c == 2:
                return True
        return False

    def has_two_pairs(self):
        self.rank_hist()
        cnt = 0
        for c in self.ranks.values():
            if c == 2:
                cnt += 1
        return cnt > 1

    def has_three(self):
        self.rank_hist()
        c = 0
        for c in self.ranks.values():
            if c == 3:
                return True
        return False

    def has_straight(self):
        self.sort()
        card_list = list(set([card.rank for card in self.cards] + [14 for card in self.cards if card.rank  == 1 ]))
        # print(card_list)
        straight = False
        for j in range(len(card_list)-4):
            straight = straight or (all(card_list[i+j] + 1 == card_list[i +j + 1] for i in range(4)))
            # print((all(card_list[i+j] + 1 == card_list[i +j + 1] for i in range(4))))
        return straight


    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        return self.has_pair() and self.has_three()

    def has_four(self):
        self.rank_hist()
        for c in self.ranks.values():
            if c == 4:
                return True
        return False

    def has_straight_flush(self):
        self.sort()
        card_list = ([(card.suit, card.rank) for card in self.cards]+[ (card.suit, 14) for card in self.cards if card.rank  == 1 ])
        card_list.sort()
        # print(card_list)
        straight = False
        for j in range(len(card_list)-4):
            straight = straight or (all(card_list[i+j][1] + 1 == card_list[i +j + 1][1] and card_list[i+j][0]  == card_list[i +j + 1][0] for i in range(4)))

        return straight

    def classify(self):

        res = [
        self.has_pair() * 1,
        self.has_two_pairs() *2,
        self.has_three() *3,
        self.has_straight() *4,
        self.has_flush() *5,
        self.has_full_house() *6,
        self.has_four() *7,
        self.has_straight_flush() *8
        ]
        key = max(res)
        # print(f'max(res) = {max(res)}')
        label = PokerHand.poker_hands[max(res)] if max(res) !=0 else 'high_card'
        self.label = label


class PokerDeck(Deck):

    def deal_hands(self, hands_num, cards_num):
        players = []
        for i in range(hands_num):
            player = PokerHand()
            self.shuffle()
            self.move_cards(player, cards_num)
            player.classify()
            players.append(player)
        return players


def probs(decks_num = 10000, hands_num = 10, cards_num = 5):
    poker_hands = {}
    for _ in range(decks_num):
        deck = PokerDeck()
        deck.shuffle()
        hands = deck.deal_hands(hands_num, cards_num)
        # print(hands)

        for hand in hands:
            poker_hands[hand.label] = poker_hands.get(hand.label, 0) + 1

    print(poker_hands)

    df = pd.DataFrame([poker_hands])
    df_t = df.transpose()
    df_t.columns = ['values']

    df_t['Percentage'] = (df_t['values'] / df_t['values'].sum()) * 100
    df_t = df_t.sort_values(by='values', ascending=False)
    print(df_t)

if __name__ == '__main__':
    probs()

