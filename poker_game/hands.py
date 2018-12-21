#!/usr/bin/env python2
"""
Hands
=====
Contains functions that given a set of hands and the community cards,
determines which five card hands the each player has.
"""

"""
Cards represented as one character for value and second character as suit.
A -> Ace
T -> 10
J -> Jack

S -> Spades
H -> Hearts
C -> Clubs
D -> Diamond
"""
CARD_STRINGS = [
    'AS',
    '2S',
    '3S',
    '4S',
    '5S',
    '6S',
    '7S',
    '8S',
    '9S',
    'TS',
    'JS',
    'QS',
    'KS',
    'AH',
    '2H',
    '3H',
    '4H',
    '5H',
    '6H',
    '7H',
    '8H',
    '9H',
    'TH',
    'JH',
    'QH',
    'KH',
    'AC',
    '2C',
    '3C',
    '4C',
    '5C',
    '6C',
    '7C',
    '8C',
    '9C',
    'TC',
    'JC',
    'QC',
    'KC',
    'AD',
    '2D',
    '3D',
    '4D',
    '5D',
    '6D',
    '7D',
    '8D',
    '9D',
    'TD',
    'JD',
    'QD',
    'KD'
]


def find_pairs(hand, community):
    """
    Determines if this hand has any pairs and if so, returns the pair and top
        three kicker or top two pairs and the top kicker.

    Note:
        When a three-of-a-kind happens, 3 pairs should be found all of the
        same number. This is not the best way to handle this.

    Args:
        hand(list(str)): A list of two strings representing two cards.
        community(list(str)): A list of 0, 3, 4, or 5 strings representing the
            cards shared in the community.

    Returns:
        list(list(str)) | None: A list of lists of strings representing the
            pairs found or `None` representing that no pairs were found.
    Note:
        The returns comes in three forms:
            None: No pairs were found.
            list( list(str,str), list(str,str,str)): The first list is the
                pair, the second are the top three kickers.
            list( list(str,str), list(str,str), list(str)): The first list is
                the highest pair, the second is the second highest, and the
                last list is the highest kicker.
    """
    return None


def main():
    hand = ['2S', '7D']
    community = ['2H', '7S', 'AS']

    print(find_pairs(hand, community))


if __name__ == '__main__':
    main()
