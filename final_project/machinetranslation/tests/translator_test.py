# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:02:54 2023

@author: cinde
"""

import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglich(unittest.TestCase):
    "This class contains the test function for testing the eng-fr translation"
    def test1(self):
        "test the en-fr translation"
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Hello"),"Adieu")

class TestEnglishToFrench(unittest.TestCase):
    "This class contains the test function for testing the fr-en translation"
    def test1(self):
        "test the fr-en translation"
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Adieu"),"Hello")

unittest.main()
