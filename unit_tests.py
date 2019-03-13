#!/usr/bin/python3

import unittest
from fizzbuzz import replace

nums, A = [], []
with open('tests.txt') as file:
	for line in file:
		nums.append(line[:line.find(' ')])
		A.append(list(map(str, line[line.find(' ') + 1:].split())))

class TestFizzbuzz(unittest.TestCase, nums, A):
	def test_fizzbuzz(self, nums, A):
		for i in range(len(nums)):
			f = replace(nums[i])
			self.assertEqual(f, A[i])

if __name__=="__main__":
	unittest.main(nums, A)
