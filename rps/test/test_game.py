#!/usr/bin/env python
# coding: utf-8

import unittest
import mock
from unittest.mock import MagicMock
from unittest_data_provider import data_provider
from rps.game import RPS


class TestGame(unittest.TestCase):

    choices = ['r', 'p', 's']
    results = ['You won!', 'You lost!', 'Tie']

    dp = lambda: (
        ('p', 'r', 'You won!'),
        ('r', 's', 'You won!'),
        ('s', 'p', 'You won!'),
        ('r', 'p', 'You lost!'),
        ('s', 'r', 'You lost!'),
        ('p', 's', 'You lost!'),
        ('p', 'p', 'Tie'),
        ('r', 'r', 'Tie'),
        ('s', 's', 'Tie'),
    )

    def setUp(self):
        self.game = RPS()

    @data_provider(dp)
    def test_run(self, x, y, z):
        self.game.select = MagicMock(return_value=x)
        self.game.rand = MagicMock(return_value=y)
        self.assertEqual((x, y, z), self.game.play())

    @data_provider(dp)
    def test_resolve(self, x, y, z):
        self.assertEqual(z, self.game.resolve(x, y))

    def test_play(self):
        self.game.select = MagicMock(return_value='s')
        _, y, z = self.game.play()
        self.assertIn(y, self.choices)
        self.assertIn(z, self.results)

    def test_select(self):
        with mock.patch('builtins.input', return_value='p'):
            self.assertEqual('p', self.game.select())


if __name__ == '__main__':
    unittest.main(verbosity=2)
