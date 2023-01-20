# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:02:54 2023

@author: cinde
"""

from pylab import *
import unittest
from translator import english_to_french, french_to_english

class test_frenchToEnglich(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertIsNone(englishToFrench("Hello"))
class test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertIsNone(frenchToEnglish("Bonjour"))

unittest.main()
