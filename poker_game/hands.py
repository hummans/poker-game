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

s -> Spades
h -> Hearts
c -> Clubs
d -> Diamond
"""
CARD_STRINGS = [
    'As',
    '2s',
    '3s',
    '4s',
    '5s',
    '6s',
    '7s',
    '8s',
    '9s',
    'Ts',
    'Js',
    'Qs',
    'Ks',
    'Ah',
    '2h',
    '3h',
    '4h',
    '5h',
    '6h',
    '7h',
    '8h',
    '9h',
    'Th',
    'Jh',
    'Qh',
    'Kh',
    'Ac',
    '2c',
    '3c',
    '4c',
    '5c',
    '6c',
    '7c',
    '8c',
    '9c',
    'Tc',
    'Jc',
    'Qc',
    'Kc',
    'Ad',
    '2d',
    '3d',
    '4d',
    '5d',
    '6d',
    '7d',
    '8d',
    '9d',
    'Td',
    'Jd',
    'Qd',
    'Kd'
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


def find_n_kickers(cards, used, n):
    """
    Finds the top n kickers that are not already used.

    Args:
        cards(list(str)): A list of card strings sorted by ordinal value.
        used(set(str)): A set of strings that have been used.
        n(int): The number of cards to find.

    Returns:
        list(str): A list with the top n cards that are not used.
    """

    kickers = []

    # Start with the highest to lowest cards.
    for card in cards:
        # If the card has already been used, skip it.
        if card in used:
            continue

        # Add the card.
        kickers.append(card)

        # If we hit the desired amount, stop.
        if len(kickers) == n:
            return kickers


NUM_KICKERS_ONE_PAIR = 3
NUM_KICKERS_TWO_PAIR = 1


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

    # Contains card values we have seen for finding pairs.
    seen = set()

    # Contains cards that have been used already for a pair.
    used = set()

    # Add each card to a seem set and if we have already seen it, then it is
    # part of a pair.
    for idx, card in enumerate(combined):
        value = get_ordinal(card)
        # If we have seen it, it is a pair with the one before it.
        if value in seen:
            prev_card = combined[idx - 1]
            pair = [card, prev_card]

            # Add both cards to used set.
            used.add(prev_card)
            used.add(card)

            # Initilialize pairs list to an empty list.
            if pairs is None:
                pairs = []

            # Add the pair.
            pairs.append(pair)

            # If we found the top two pairs, stop.
            if len(pairs) == 2:
                break
        # Add value to seen, for future.
        seen.add(value)

    # Find top kickers.
    if pairs is None:
        # If no pair is found, we do not need to find kickers.
        pass
    elif len(pairs) == 1:
        # One pair needs to find three kickers.
        kickers = find_n_kickers(combined, used, NUM_KICKERS_ONE_PAIR)
        pairs.append(kickers)
    elif len(pairs) == 2:
        # Two pair needs to find one kicker.
        kickers = find_n_kickers(combined, used, NUM_KICKERS_TWO_PAIR)
        pairs.append(kickers)
    else:
        raise RuntimeError(
            "More than two pairs found. List: '{}'".format(pairs)
        )

    return pairs


def main():
    hole_cards = ['2S', '7D']
    community = ['2H', '7S', 'AS']

    print(find_pairs(hole_cards, community))


if __name__ == '__main__':
    main()
