'''
Created on Oct 1, 2014

@author: pirmin
'''
from unittest import TestCase
from src.TECH.StringUtils import StringUtils

class TestStringUtils(TestCase):
    def test_reverse(self):
        basic_string = "annelien"
        string_utils_object = StringUtils()
        reversed_basic_string = string_utils_object.reverse(basic_string)
        self.assertEqual(reversed_basic_string, "neilenna")