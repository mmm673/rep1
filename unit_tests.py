#!/usr/bin/python3

import unittest
from fizzbuzz import replace

class TestFizzbuzz(unittest.TestCase):
  def test_fizzbuzz(self):
    f = replace(5)
    self.assertEqual(f, [1, 3, 'fizz', 4, 'buzz'])

if __name__=="__main__":
  unittest.main()
