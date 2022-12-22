# -*- coding: utf-8 -*-
from strategy import *
from factory_strategy import FactoryStrategy
from gilded_rose import GildedRose
from golden_master import golden_master_to_string
from item import Item
import unittest


class GildedRoseTest(unittest.TestCase):

    def test_golden_master(self):
        text_file = open("original_30_days.txt", "r")
        expected = text_file.read()
        text_file.close()

        actual = golden_master_to_string(31)
        self.assertEqual(expected, actual)

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sulfarus_legendary_unchanged(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = ["Sulfuras, Hand of Ragnaros", 0, 80]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item(self):
        items = [Item("Elixir of the Mongoose", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", 9, 24]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_out_of_date(self):
        items = [Item("Elixir of the Mongoose", -5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", -6, 23]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_fives_times(self):
        items = [Item("Elixir of the Mongoose", 10, 25)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", 5, 20]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_fives_times_entering_out_of_date(self):
        items = [Item("Elixir of the Mongoose", 2, 25)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", -3, 17]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_fives_times_out_of_date(self):
        items = [Item("Elixir of the Mongoose", -2, 25)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", -7, 15]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_brie_out_of_date(self):
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Aged Brie", -2, 22]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_brie_quality_over_50(self):
        items = [Item("Aged Brie", -1, 45)]
        gilded_rose = GildedRose(items)
        for i in range(10):
            gilded_rose.update_quality()

        expected = ["Aged Brie", -11, 50]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_going_out_of_date_tickets(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Backstage passes to a TAFKAL80ETC concert", -1, 0]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_already_out_of_date_tickets(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Backstage passes to a TAFKAL80ETC concert", -3, 0]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_factory_build_single_item(self):
        factory = FactoryStrategy()
        single_input = ["Elixir of the Mongoose", 10, 25]

        actual = type(factory.get_strategy(single_input))
        expected = type(Item("Elixir of the Mongoose", 10, 25))

        self.assertEqual(expected, actual)

    def test_factory_build_one_item_of_each_type(self):
        factory = FactoryStrategy()
        inputs = [
            ["Aged Brie", 2, 0],
            ["Elixir of the Mongoose", 5, 7],
            ["Sulfuras, Hand of Ragnaros", 0, 80],
            ["Backstage passes to a TAFKAL80ETC concert", 15, 20]]

        items = list(map(Item.get_strategy(factory), inputs))

        items_2 = [
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
            ]

        actual = list(map(type, items))
        expected = list(map(type, items_2))

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
