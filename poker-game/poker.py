"""
Poker Engine
"""
import random
from math import floor

# Mapping Ace to King

# 0-12:     Diamonds
# 13-25:    Clubs
# 26-38:    Hearts
# 39-51:    Spades


class Card(object):
    CARD_RANGE = 13
    VALUES = list(range(CARD_RANGE))
    DIAMONDS = 'D'
    CLUBS = 'C'
    HEARTS = 'H'
    SPADES = 'S'

    RED = 'r'
    BLACK = 'b'

    SUITS = [DIAMONDS, CLUBS, HEARTS, SPADES]
    REDS = [DIAMONDS, HEARTS]
    BLACKS = [CLUBS, SPADES]

    SUIT_NAMES = {
        DIAMONDS: 'Diamonds',
        CLUBS: 'Clubs',
        HEARTS: 'Hearts',
        SPADES: 'Spades'
    }

    VALUE_NAMES = [
            'Ace',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'Jack',
            'Queen',
            'King']

    def __init__(self, id_):
        self.id = id_
        self.set_value()
        self.set_suit()
        self.set_name()
        self.color = Card.RED if self.suit in Card.REDS else Card.BLACK

    def set_value(self):
        self.value = self.id % Card.CARD_RANGE

    def set_suit(self):
        suit_num = int(floor(self.id / Card.CARD_RANGE))
        self.suit = Card.SUITS[suit_num]
        self.suit_name = Card.SUIT_NAMES[self.suit]

    def set_name(self):
        self.name = Card.VALUE_NAMES[self.value]
        self.full_name = "{card.name} of {card.suit_name}".format(card=self)

    def __str__(self):
        return self.full_name


class Hand(object):

    def __init__(self, cards):
        self.card_1 = cards[0]
        self.card_2 = cards[1]

    def __str__(self):
        hand_str = (
            "Hand:\n"
            "Card 1: {hand.card_1}\n"
            "Card 2: {hand.card_2}\n"
        ).format(hand=self)
        return hand_str


class Community(object):

    MAX_TURN = 3

    # States
    PREFLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3

    # Names of each state.
    STATE_NAMES = [
        "Pre-Flop",
        "Flop",
        "Turn",
        "River"
    ]

    def __init__(self, cards):
        self.state = 0
        self.flop = cards[:3]
        self.turn = cards[:4]
        self.river = cards[:]

    def next(self):
        self.state += 1
        self.state = min(self.state, Community.MAX_TURN)

    def __str__(self):
        if self.state is Community.PREFLOP:
            state_name = Community.STATE_NAMES[self.state]
            community_str = (
                "Community Cards:\n"
                "State: {state}\n"
                "HIDDEN"
            ).format(state=state_name)
        elif self.state is Community.FLOP:
            state_name = Community.STATE_NAMES[self.state]
            community_str = (
                "Community Cards:\n"
                "State: {state}\n"
                "{}\n"
                "{}\n"
                "{}"
            ).format(
                state=state_name,
                *self.flop)
        elif self.state is Community.TURN:
            state_name = Community.STATE_NAMES[self.state]
            community_str = (
                "Community Cards:\n"
                "State: {state}\n"
                "{}\n"
                "{}\n"
                "{}\n"
                "{}"
            ).format(
                state=state_name,
                *self.turn)
        elif self.state is Community.RIVER:
            state_name = Community.STATE_NAMES[self.state]
            community_str = (
                "Community Cards:\n"
                "State: {state}\n"
                "{}\n"
                "{}\n"
                "{}\n"
                "{}\n"
                "{}"
            ).format(
                state=state_name,
                *self.river)
        else:
            community_str = "ERROR"

        return community_str


class PokerEngine(object):

    NUM_CARDS = 52

    def __init__(self):
        self.cards = None

    def deal_hands(self, num_players):
        self.cards = list(range(PokerEngine.NUM_CARDS))
        random.shuffle(self.cards)
        hands = []
        for player in range(num_players):
            id_1 = self.cards.pop()
            id_2 = self.cards.pop()
            card_1 = Card(id_1)
            card_2 = Card(id_2)
            hand_cards = [card_1, card_2]
            hand = Hand(hand_cards)
            hands.append(hand)

        return hands

    def deal_community(self):
        community_cards = self.cards[:5]
        community_cards = map(Card, community_cards)
        community = Community(community_cards)
        return community


class Player(object):

    def __init__(self):
        pass


def play_game(num_players):
    pg = PokerEngine()
    hands = pg.deal_hands(num_players)
    card = Card(12)
    print(card)
    hand = hands[0]
    print(hand)
    community = pg.deal_community()
    print(community)
    community.next()
    print(community)


def main():
    num_players = 10
    pg = PokerEngine()
    hands = pg.deal_hands(num_players)
    card = Card(12)
    print(card)
    hand = hands[0]
    print(hand)
    community = pg.deal_community()
    print(community)
    community.next()
    print(community)


if __name__ == '__main__':
    main()
