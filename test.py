#!/usr/bin/env python
# coding: utf-8

import unittest


def load_tests(loader, tests, pattern):
    return loader.discover('rps')


if __name__ == '__main__':
    unittest.main(verbosity=2)
