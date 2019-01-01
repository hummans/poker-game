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
        hole_cards = ['3s', '8d']
        community = ['2h', '7s', 'As']
        pairs_corrrect = None
        pairs = hands.find_pairs(hole_cards, community)
        self.assertEqual(pairs, pairs_corrrect)

        # Test one pair.
        hole_cards = ['2s', '8d']
        community = ['2h', '7s', 'As']
        pairs_corrrect = [set(['2s', '2h']), set(['8d', '7s', 'As'])]
        pairs = hands.find_pairs(hole_cards, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

        # Test two pair.
        hole_cards = ['2s', '7d']
        community = ['2h', '7s', 'As']
        pairs_corrrect = [set(['7d', '7s']), set(['2s', '2h']), set(['As'])]
        pairs = hands.find_pairs(hole_cards, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

        # Test three pair.
        hole_cards = ['2s', '7d']
        community = ['2h', '7s', 'As', '6s', 'Ac']
        pairs_corrrect = [set(['As', 'Ac']), set(['7d', '7s']), set(['6s'])]
        pairs = hands.find_pairs(hole_cards, community)
        pairs = TestHands.to_set(pairs)
        self.assertEqual(pairs, pairs_corrrect)

    def test_find_three_of_a_kind(self):
        """
        Tests the find three-of-a-kind function.
        """
        # Test no three-of-a-kind.
        hole_cards = ['3s', '3d']
        community = ['2h', '7c', 'As']
        hand_correct = None
        hand = hands.find_three_of_a_kind(hole_cards, community)
        self.assertEqual(hand, hand_correct)

        # Test one three-of-a-kind.
        hole_cards = ['3s', '3d']
        community = ['2h', '3c', 'As']
        hand_correct = [set(['3s', '3d', '3c']), set(['2h', 'As'])]
        hand = hands.find_three_of_a_kind(hole_cards, community)
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

    def test_find_straight(self):
        """
        Tests the find straight function.
        """
        # Test no straight.
        hole_cards = ['3s', '3d']
        community = ['2h', '7c', 'As']
        hand_correct = None
        hand = hands.find_straight(hole_cards, community)
        self.assertEqual(hand, hand_correct)

        # Test one straight.
        hole_cards = ['4s', '2d']
        community = ['5h', '3c', '6s']
        hand_correct = [set(['5h', '4s', '3c', '2d', '6s'])]
        hand = [hands.find_straight(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

        # Test ace straight.
        hole_cards = ['4s', '2d']
        community = ['5h', '3c', 'As']
        hand_correct = [set(['5h', '4s', '3c', '2d', 'As'])]
        hand = [hands.find_straight(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

    def test_find_flush(self):
        """
        Tests the find flush function.
        """
        # Test no flush.
        hole_cards = ['3s', '3d']
        community = ['2h', '7c', 'As']
        hand_correct = None
        hand = hands.find_flush(hole_cards, community)
        self.assertEqual(hand, hand_correct)

        # Test one flush.
        hole_cards = ['3s', '8s']
        community = ['2s', '7s', 'As']
        hand_correct = [set(['As', '8s', '7s', '3s', '2s'])]
        hand = [hands.find_flush(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

        # Test six card flush.
        hole_cards = ['3s', '8s']
        community = ['2s', '7s', 'As', '9s', 'Jd']
        hand_correct = [set(['As', '9s', '8s', '7s', '3s'])]
        hand = [hands.find_flush(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

        # Test seven card flush.
        hole_cards = ['3s', '8s']
        community = ['2s', '7s', 'As', '9s', 'Js']
        hand_correct = [set(['As', 'Js', '9s', '8s', '7s'])]
        hand = [hands.find_flush(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

    def test_find_straight_flush(self):
        """
        Tests the find straight-flush function.
        """
        # Test no straight_flush.
        hole_cards = ['3s', '3d']
        community = ['2h', '7c', 'As']
        hand_correct = None
        hand = hands.find_straight_flush(hole_cards, community)
        self.assertEqual(hand, hand_correct)

        # Test one straight_flush.
        hole_cards = ['3s', '5s']
        community = ['2s', '4s', 'As']
        hand_correct = [set(['5s', '4s', '3s', '2s', 'As'])]
        hand = [hands.find_straight_flush(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

        # Test six card straight_flush.
        hole_cards = ['Ts', '9s']
        community = ['7s', '8s', '5s', '6s', 'Jd']
        hand_correct = [set(['Ts', '9s', '8s', '7s', '6s'])]
        hand = [hands.find_straight_flush(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)

        # Test seven card straight_flush.
        hole_cards = ['Ts', '9s']
        community = ['7s', '8s', '5s', '6s', 'Js']
        hand_correct = [set(['Js', 'Ts', '9s', '8s', '7s'])]
        hand = [hands.find_straight_flush(hole_cards, community)]
        hand = TestHands.to_set(hand)
        self.assertEqual(hand, hand_correct)


if __name__ == '__main__':
    unittest.main()
