from django.test import TestCase

from app.calc import add

"""Tests must be in file that starts with test, all test functions must start with test as well """
class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8), 11)