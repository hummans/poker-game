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
        hand = ['3S', '8D']
        community = ['2H', '7S', 'AS']
        pairs_corrrect = None
        pairs = hands.find_pairs(hand, community)
        self.assertEqual(pairs, pairs_corrrect)

        # Test one pair.
        hand = ['2S', '8D']
        community = ['2H', '7S', 'AS']
        pairs_corrrect = [set(['2S', '2H']), set(['8D', '7S', 'AS'])]
        pairs = hands.find_pairs(hand, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)
        # Test two pair.
        hand = ['2S', '7D']
        community = ['2H', '7S', 'AS']
        pairs_corrrect = [set(['7D', '7S']), set(['2S', '2H']), set(['AS'])]
        pairs = hands.find_pairs(hand, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

        # Test three pair.
        hand = ['2S', '7D']
        community = ['2H', '7S', 'AS', '6S', 'AC']
        pairs_corrrect = [set(['AS', 'AC']), set(['7D', '7S']), set(['6S'])]
        pairs = hands.find_pairs(hand, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)


if __name__ == '__main__':
    unittest.main()
