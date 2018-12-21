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


def to_value(card):
    """
    Returns the value of the card.

    Args:
        card(str): A two character string with value then suit.

    Returns:
        str: The first character of the string.
    """
    return card[0]


def get_ordinal(card):
    """
    Converts card to numerical value. 2 is 2 and A is 14.

    Args:
        card(str): A two character string with value then suit.

    Returns:
        int: The ordinal value of the card.
    """
    # Get first char that represents value.
    value_str = to_value(card)

    # For all cards that do not have an int.
    str_to_int = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    if value_str not in str_to_int:
        return int(value_str)
    else:
        return str_to_int[value_str]


def find_pairs(hole_cards, community):
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
    # Initialize pairs to None as default return value.
    pairs = None

    # Combine hole_cards and community because does not matter where they are
    # from.
    hole_cards.extend(community)
    combined = hole_cards

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)
    print(combined)

    # Add each card to a set and if we have already seen it, then it is part
    # of a pair.
    seen = set()
    used = set()
    for idx, card in enumerate(combined):
        value = get_ordinal(card)
        # If we have seen it, it is a pair with the one before it.
        if value in seen:
            prev_card = combined[idx - 1]
            pair = [card, prev_card]
            used.add(prev_card)
            used.add(card)
            if pairs is None:
                pairs = []
            pairs.append(pair)
            if len(pairs) == 2:
                break
        seen.add(value)

    # Find top kickers.
    if pairs is None:
        return pairs
    elif len(pairs) == 1:
        kickers = []
        for card in combined:
            if card in used:
                continue
            kickers.append(card)
            if len(kickers) == 3:
                pairs.append(kickers)
                break
    elif len(pairs) == 2:
        kickers = []
        for card in combined:
            if card in used:
                continue
            kickers.append(card)
            if len(kickers) == 1:
                pairs.append(kickers)
                break
    elif len(pairs) == 3:
        pass
    else:
        raise RuntimeError(
            "More than three pairs found. List: '{}'".format(pairs)
        )

    return pairs


def main():
    hole_cards = ['2S', '7D']
    community = ['2H', '7S', 'AS']

    print(find_pairs(hole_cards, community))


if __name__ == '__main__':
    main()
