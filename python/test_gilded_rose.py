# -*- coding: utf-8 -*-
from factory import Factory
from gilded_rose import *
from item_classes import *
from golden_master import golden_master_to_string
import unittest


class GildedRoseTest(unittest.TestCase):

    def test_golden_master(self):
        text_file = open("original_30_days.txt", "r")
        expected = text_file.read()
        text_file.close()

        actual = golden_master_to_string(31)
        self.assertEqual(expected, actual)

    def test_foo(self):
        items = [Basic("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sulfarus_legendary_unchanged(self):
        items = [Legendary("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = ["Sulfuras, Hand of Ragnaros", 0, 80]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item(self):
        items = [Basic("Elixir of the Mongoose", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", 9, 24]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_out_of_date(self):
        items = [Basic("Elixir of the Mongoose", -5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", -6, 23]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_fives_times(self):
        items = [Basic("Elixir of the Mongoose", 10, 25)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", 5, 20]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_fives_times_entering_out_of_date(self):
        items = [Basic("Elixir of the Mongoose", 2, 25)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", -3, 17]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_basic_item_fives_times_out_of_date(self):
        items = [Basic("Elixir of the Mongoose", -2, 25)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()

        expected = ["Elixir of the Mongoose", -7, 15]

        self.assertEqual(expected[0], items[0].name)
        self.assertEqual(expected[1], items[0].sell_in)
        self.assertEqual(expected[2], items[0].quality)

    def test_brie_out_of_date(self):
        items = [Brie("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Aged Brie", -2, 22]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_brie_quality_over_50(self):
        items = [Brie("Aged Brie", -1, 45)]
        gilded_rose = GildedRose(items)
        for i in range(10):
            gilded_rose.update_quality()

        expected = ["Aged Brie", -11, 50]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_going_out_of_date_tickets(self):
        items = [Backstage("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Backstage passes to a TAFKAL80ETC concert", -1, 0]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_already_out_of_date_tickets(self):
        items = [Backstage("Backstage passes to a TAFKAL80ETC concert", -2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected = ["Backstage passes to a TAFKAL80ETC concert", -3, 0]

        self.assertEqual(expected[0], gilded_rose.items[0].name)
        self.assertEqual(expected[1], gilded_rose.items[0].sell_in)
        self.assertEqual(expected[2], gilded_rose.items[0].quality)

    def test_factory_build_single_item(self):
        factory = Factory()
        single_input = ["Elixir of the Mongoose", 10, 25]

        actual = type(factory.build_item(single_input))
        expected = type(Basic("Elixir of the Mongoose", 10, 25))

        self.assertEqual(expected, actual)

    def test_factory_build_one_item_of_each_type(self):
        factory = Factory()
        inputs = [
            ["Aged Brie", 2, 0],
            ["Elixir of the Mongoose", 5, 7],
            ["Sulfuras, Hand of Ragnaros", 0, 80],
            ["Backstage passes to a TAFKAL80ETC concert", 15, 20]]

        items = list(map(factory.build_item, inputs))

        items_2 = [
            Brie(name="Aged Brie", sell_in=2, quality=0),
            Basic(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Legendary(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
            ]

        actual = list(map(type, items))
        expected = list(map(type, items_2))

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
