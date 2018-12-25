#!/usr/bin/env python2
"""
Test Hands
==========

Test that the Hands functions correctly identify hands.
"""
import sys
import os
# Adds the path of poker_game to test file.
sys.path.append(os.path.join(os.path.dirname(__name__), '..'))

import unittest
from poker_game import hands


class TestHands(unittest.TestCase):

    @staticmethod
    def to_set(hand):
        try:
            for idx, list_ in enumerate(hand):
                hand[idx] = set(list_)
        except TypeError:
            pass
        return hand

    def test_find_pairs(self):
        """
        Tests the find pairs function.
        """
        # Test no pairs.
        hole_cards = ['3S', '8D']
        community = ['2H', '7S', 'AS']
        pairs_corrrect = None
        pairs = hands.find_pairs(hole_cards, community)
        self.assertEqual(pairs, pairs_corrrect)

        # Test one pair.
        hole_cards = ['2S', '8D']
        community = ['2H', '7S', 'AS']
        pairs_corrrect = [set(['2S', '2H']), set(['8D', '7S', 'AS'])]
        pairs = hands.find_pairs(hole_cards, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

        # Test two pair.
        hole_cards = ['2S', '7D']
        community = ['2H', '7S', 'AS']
        pairs_corrrect = [set(['7D', '7S']), set(['2S', '2H']), set(['AS'])]
        pairs = hands.find_pairs(hole_cards, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

        # Test three pair.
        hole_cards = ['2S', '7D']
        community = ['2H', '7S', 'AS', '6S', 'AC']
        pairs_corrrect = [set(['AS', 'AC']), set(['7D', '7S']), set(['6S'])]
        pairs = hands.find_pairs(hole_cards, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

    def test_find_three_of_a_kind(self):
        """
        Tests the find three-of-a-kind function.
        """
        # Test no three-of-a-kind.
        hole_cards = ['3S', '3D']
        community = ['2H', '7C', 'AS']
        hand_correct = None
        hand = hands.find_three_of_a_kind(hole_cards, community)
        self.assertEqual(hand, hand_correct)

        # Test one three-of-a-kind.
        hole_cards = ['3S', '3D']
        community = ['2H', '3C', 'AS']
        hand_correct = [set(['3S', '3D', '3C']), set(['2H', 'AS'])]
        hand = hands.find_three_of_a_kind(hole_cards, community)
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)


if __name__ == '__main__':
    unittest.main()
