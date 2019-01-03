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


def to_suit(card):
    """
        Returns the suit of the card.

        Args:
            card(str): A two character string with value then suit.

        Returns:
            str: The second character of the string.
        """
    return card[1].lower()


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


def get_suit(card):
    """
        Converts suit to numerical value.
        Diamond is 0
        Club is 1
        Heart is 2
        Spade is 3

        Args:
            card(str): A two character string with value then suit.

        Returns:
            int: The suit of the card in numerical form.
        """
    value_suit = to_suit(card)
    suit_to_int = {
        'd': 0,
        'c': 1,
        'h': 2,
        's': 3
    }

    return suit_to_int[value_suit]


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
        hole_cards(list(str)): A list of two strings representing two cards.
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
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

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


NUM_KICKERS_THREE_OF_A_KIND = 2


def find_three_of_a_kind(hole_cards, community):
    """
    Finds a three-of-a-kind and two best kickers. Returns `None` if no three of
        a kind is found.

    Note:
        Assumes that there is no four-of-a-kind or full-house possible.

    Args:
        hole_cards(list(str)): A list of two strings representing two cards.
        community(list(str)): A list of 0, 3, 4, or 5 strings representing the
            cards shared in the community.

    Returns:
        list(list(str)) | None: A list of lists of strings representing the
            three-of-a-kind found or `None` representing that no
            three-of-a-kind was found.
    Note:
        The returns comes in two forms:
            None: No three-of-a-kind was found.
            list( list(str,str,str), list(str,str)): The first list is the
                three-of-a-kind, the second is the top two kickers.
    """
    # Initialize hand to empty list.
    hand = []

    # Combine hole_cards and community because does not matter where they are
    # from.
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)

    # Map of card value to count seen.
    card_count = {}

    # Contains cards that have been already used in the hand.
    used = set()

    # Count each card into card count and look for three-of-a-kind.
    for idx, card in enumerate(combined):
        # Grab the value of the card ignoring suit.
        value = get_ordinal(card)

        # If the value is not in the map initialize it to 0.
        if value not in card_count:
            card_count[value] = 0

        # Increment count of this value of card.
        card_count[value] += 1

        # Checking if we found the three-of-a-kind.
        if card_count[value] == 3:
            start = idx - 2
            end = idx + 1

            # Because it is sorted we can grab the last three cards seen.
            three_of_a_kind = combined[start:end]

            # Add three-of-a-kind to used set.
            used.update(three_of_a_kind)

            # Add three-of-a-kind to hand.
            hand.append(three_of_a_kind)
            break

    # No three-of-a-kind was found, return None.
    if not hand:
        return None

    # We have found a three-of-a-kind, we find the top two kickers.
    kickers = find_n_kickers(combined, used, NUM_KICKERS_THREE_OF_A_KIND)

    # Add the kickers to the hand.
    hand.append(kickers)

    return hand


def find_straight(hole_cards, community):
    """
        Finds a straight. Returns `None` if no straight is found.


        Args:
            hole_cards(list(str)): A list of two strings representing two
                cards.
            community(list(str)): A list of 0, 3, 4, or 5 strings representing
                the cards shared in the community.

        Returns:
            list(list(str)) | None: A list of lists of strings representing the
                straight found or `None` representing that no
                straight was found.
        Note:
            The returns comes in two forms:
                None: No straight was found.
                list( list(str,str,str,str,str)): The highest straight found.
    """

    # Initialize hand to empty list.
    hand = []

    # Combine hole_cards and community because does not matter where they are
    # from.
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)

    # previous card value
    value = 0

    # iterate from highest card to lowest
    for card in combined:
        # add the card to the hand
        hand.append(card)
        # first iteration just set as previous card value then continue
        if value != 0:
            # if the current card is 1 smaller than the last card
            if get_ordinal(card) == value - 1:
                # if the hand is already 5 cards then we are done
                if len(hand) == 5:
                    return hand
                # edge case of straight 5 high
                elif len(hand) == 4 and get_ordinal(card) == 2:
                    # when the cards are 5 4 3 2 check if there is an ace
                    if get_ordinal(combined[0]) == 14:
                        hand.append(combined[0])
                        return hand
            # if the last card is the same value as the current card
            elif get_ordinal(card) == value:
                # delete the current card and move on
                hand.pop()
                continue
            # the card has a gap from the previous card
            else:
                # restart the hand
                hand = [card]
        # set the previous card value then back to top of loop
        value = get_ordinal(card)

    # if there is no straight found, return None
    return None


def find_flush(hole_cards, community):
    """
        Finds a flush. Returns `None` if no flush is found.

        Args:
            hole_cards(list(str)): A list of two strings representing two
                cards.
            community(list(str)): A list of 0, 3, 4, or 5 strings representing
                the cards shared in the community.

        Returns:
            list(list(str)) | None: A list of lists of strings representing the
                flush or `None` representing that no flush was found.
        Note:
            The returns comes in two forms:
                None: No flush was found.
                list( list(str,str,str,str,str)): The highest flush found.
    """
    # create lists to sort each suit, hand[0] is list of diamonds, etc.
    hand = [[], [], [], []]

    # Combine hole_cards and community because does not matter where they are
    # from.
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)

    # iterate from highest card to lowest
    for card in combined:
        # find the suit of the card
        suit = get_suit(card)
        # add card to list of card of that suit
        hand[suit].append(card)
        # return if a suit has 5 cards
        if len(hand[suit]) == 5:
            return hand[suit]

    # no suit has 5 cards
    return None


def find_full_house(hole_cards, community):
    """
    Finds a full-house. Returns `None` if no full-house is found.

    Args:
        hole_cards(list(str)): A list of two strings representing two cards.
        community(list(str)): A list of 0, 3, 4, or 5 strings representing the
            cards shared in the community.

    Returns:
        list(list(str)) | None: A list of lists of strings representing the
            full-house found or `None` representing that no full-house was
            found.
    Note:
        The returns comes in two forms:
            None: No full-house was found.
            list( list(str,str,str), list(str,str) ): The first list is the
                three-of-a-kind, the second is the top pair.
    """
    # Initialize hand to empty list.
    hand = []

    # Combine hole_cards and community because does not matter where they are
    # from.
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)

    # Find three-of-a-kind.
    three_of_a_kind_hand = find_three_of_a_kind(combined, [])

    # If there is not a three-of-a-kind, a full-house is not possible.
    if three_of_a_kind_hand is None:
        return None

    # Get the list representing the three-of-a-kind.
    three_of_a_kind = three_of_a_kind_hand[0]

    # Remove the used cards from the available cards.
    for card in three_of_a_kind:
        combined.remove(card)

    # Find pair.
    pair_hand = find_pairs(combined, [])

    # If there is not a pair, a full-house is not possible.
    if pair_hand is None:
        return None

    # Get the list representing the top pair.
    pair = pair_hand[0]

    # Format the full-house.
    hand = [three_of_a_kind, pair]

    return hand


NUM_KICKERS_FOUR_OF_A_KIND = 1


def find_four_of_a_kind(hole_cards, community):
    """
    Finds a four-of-a-kind and two best kickers. Returns `None` if no four of
        a kind is found.

    Note:
        Assumes that there is no four-of-a-kind or full-house possible.

    Args:
        hole_cards(list(str)): A list of two strings representing two cards.
        community(list(str)): A list of 0, 3, 4, or 5 strings representing the
            cards shared in the community.

    Returns:
        list(list(str)) | None: A list of lists of strings representing the
            four-of-a-kind found or `None` representing that no
            four-of-a-kind was found.
    Note:
        The returns comes in two forms:
            None: No four-of-a-kind was found.
            list( list(str,str,str,str), list(str)): The first list is the
                four-of-a-kind, the second is the top kicker.
    """
    # Initialize hand to empty list.
    hand = []

    # Combine hole_cards and community because does not matter where they are
    # from.
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)

    # Map of card value to count seen.
    card_count = {}

    # Contains cards that have been already used in the hand.
    used = set()

    # Count each card into card count and look for four-of-a-kind.
    for idx, card in enumerate(combined):
        # Grab the value of the card ignoring suit.
        value = get_ordinal(card)

        # If the value is not in the map initialize it to 0.
        if value not in card_count:
            card_count[value] = 0

        # Increment count of this value of card.
        card_count[value] += 1

        # Checking if we found the four-of-a-kind.
        if card_count[value] == 4:
            start = idx - 3
            end = idx + 1

            # Because it is sorted we can grab the last four cards seen.
            three_of_a_kind = combined[start:end]

            # Add four-of-a-kind to used set.
            used.update(three_of_a_kind)

            # Add four-of-a-kind to hand.
            hand.append(three_of_a_kind)
            break

    # No four-of-a-kind was found, return None.
    if not hand:
        return None

    # We have found a four-of-a-kind, we find the top two kickers.
    kickers = find_n_kickers(combined, used, NUM_KICKERS_FOUR_OF_A_KIND)

    # Add the kickers to the hand.
    hand.append(kickers)

    return hand


def find_straight_flush(hole_cards, community):
    """
        Finds a straight flush. Returns `None` if no flush is found.

        Args:
            hole_cards(list(str)): A list of two strings representing two
                cards.
            community(list(str)): A list of 0, 3, 4, or 5 strings representing
                the cards shared in the community.

        Returns:
            list(list(str)) | None: A list of lists of strings representing the
                straight flush or `None` representing that no straight flush
                was found.
        Note:
            The returns comes in two forms:
                None: No straight flush was found.
                list( list(str,str,str,str,str)): The highest straight flush
                    found.
    """
    # create lists to sort each suit, hand[0] is list of diamonds, etc.
    hand = [[], [], [], []]

    # Combine hole_cards and community because does not matter where they are
    # from.
    combined = []
    combined.extend(hole_cards)
    combined.extend(community)

    # Sort the cards from highest to lowest.
    combined.sort(reverse=True, key=get_ordinal)

    # iterate from highest card to lowest
    for card in combined:
        # find the suit of the card
        suit = get_suit(card)
        # add card to list of card of that suit
        hand[suit].append(card)

    # now that all the suits are sorted, find a straight in the suit
    for suits in hand:
        # only 1 suit can have more than 5 cards, so find a straight in that
        # suit
        if len(suits) >= 5:
            return find_straight(suits, [])


def hand_comparator(combined_a, combined_b):
    """
    Compares two hands.

    Args:
        combined(list(str)): A list of seven cards representing hole_cards
            combined with the community. Assumes sorted high to low.

    Returns:
        int: Represents the difference in strength between the two hands.

    Note:
        The returns has three possibilities:
            -1 : Meaning the second hand is stronger.
            0 : Meaning the hands are equal in strength.
            1 : Meaning the the first hand is stronger.
        Acts like `return b - a`.

    """
    pass


def comparator(hole_cards_zero, hole_cards_one, community):
    """
    Compares two sets of hole cards and sees which is stronger.
    """

    """
    straight flush
    """
    best_zero = find_straight_flush(hole_cards_zero, community)
    best_one = find_straight_flush(hole_cards_one, community)

    # check if both hands have a straight flush
    if best_zero is not None and best_one is not None:
        # find how high straight flush is
        card_zero = get_ordinal(best_zero[0])
        card_one = get_ordinal(best_one[0])
        if card_one > card_zero:
            return -1
        elif card_one < card_zero:
            return 1
        else:
            # both hands are same
            return 0
    # if first player has straight flush but second does not
    if best_zero is None and best_one is not None:
        return -1
    # if second player has straight flush but first does not
    elif best_one is None and best_zero is not None:
        return 1

    """
    quads
    """
    # check if both hands have a quad
    best_zero = find_four_of_a_kind(hole_cards_zero, community)
    best_one = find_four_of_a_kind(hole_cards_one, community)
    if best_zero is not None and best_one is not None:
        # find what quad it is
        card_zero = get_ordinal(best_zero[0][0])
        card_one = get_ordinal(best_one[0][0])
        if card_one > card_zero:
            return -1
        elif card_one < card_zero:
            return 1
        else:
            # find kicker
            card_zero = get_ordinal(best_zero[1][0])
            card_one = get_ordinal(best_one[1][0])
            if card_one > card_zero:
                return -1
            elif card_one < card_zero:
                return 1
            else:
                # both hands are same
                return 0
    if best_zero is None and best_one is not None:
        return -1
    elif best_one is None and best_zero is not None:
        return 1

    """
    full house
    """
    best_zero = find_full_house(hole_cards_zero, community)
    best_one = find_full_house(hole_cards_one, community)
    if best_zero is not None and best_one is not None:
        # check the value of triple in full house
        card_zero = get_ordinal(best_zero[0][0])
        card_one = get_ordinal(best_one[0][0])
        if card_one > card_zero:
            return -1
        elif card_one < card_zero:
            return 1
        else:
            # then check value of pair
            card_zero = get_ordinal(best_zero[1][0])
            card_one = get_ordinal(best_one[1][0])
            if card_one > card_zero:
                return -1
            elif card_one < card_zero:
                return 1
            else:
                # both hands are same
                return 0
    if best_zero is None and best_one is not None:
        return -1
    elif best_one is None and best_zero is not None:
        return 1

    """
    flush
    """
    best_zero = find_flush(hole_cards_zero, community)
    best_one = find_flush(hole_cards_one, community)
    if best_zero is not None and best_one is not None:
        # find highest card in flush
        card_zero = get_ordinal(best_zero[0])
        card_one = get_ordinal(best_one[0])
        if card_one > card_zero:
            return -1
        elif card_one < card_zero:
            return 1
        else:
            return 0
    if best_zero is None and best_one is not None:
        return -1
    elif best_one is None and best_zero is not None:
        return 1

    """
    straight
    """
    best_zero = find_straight(hole_cards_zero, community)
    best_one = find_straight(hole_cards_one, community)
    if best_zero is not None and best_one is not None:
        # find how high straight is
        card_zero = get_ordinal(best_zero[0])
        card_one = get_ordinal(best_one[0])
        if card_one > card_zero:
            return -1
        elif card_one < card_zero:
            return 1
        else:
            return 0
    if best_zero is None and best_one is not None:
        return -1
    elif best_one is None and best_zero is not None:
        return 1

    """
    three of a kind
    """
    best_zero = find_three_of_a_kind(hole_cards_zero, community)
    best_one = find_three_of_a_kind(hole_cards_one, community)
    if best_zero is not None and best_one is not None:
        # find what triple is
        card_zero = get_ordinal(best_zero[0][0])
        card_one = get_ordinal(best_one[0][0])
        if card_one > card_zero:
            return -1
        elif card_one < card_zero:
            return 1
        else:
            # first kicker
            card_zero = get_ordinal(best_zero[1][0])
            card_one = get_ordinal(best_one[1][0])
            if card_one > card_zero:
                return -1
            elif card_one < card_zero:
                return 1
            else:
                # second kicker
                card_zero = get_ordinal(best_zero[1][1])
                card_one = get_ordinal(best_one[1][1])
                if card_one > card_zero:
                    return -1
                elif card_one < card_zero:
                    return 1
                else:
                    return 0
    if best_zero is None and best_one is not None:
        return -1
    elif best_one is None and best_zero is not None:
        return 1


def main():
    hole_cards_zero = ['2C', 'KH']
    hole_cards_one = ['2D', '9C']
    community = ['2S', '2H', '7H', '4C', '5D']

    print(comparator(hole_cards_zero, hole_cards_one, community))


if __name__ == '__main__':
    main()
