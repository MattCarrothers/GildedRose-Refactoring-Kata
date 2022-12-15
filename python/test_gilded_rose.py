# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import golden_master_to_string


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_golden_master(self):
        text_file = open("original_30_days.txt", "r")
        expected = text_file.read()
        text_file.close()

        actual = golden_master_to_string(31)
        self.assertEqual(expected, actual)


        
if __name__ == '__main__':
    unittest.main()
