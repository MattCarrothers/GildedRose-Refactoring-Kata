from __future__ import print_function
from gilded_rose import *
from item import Item
from observer import DayCount


def update_via_observing(days):

    items = [
        Item("+5 Dexterity Vest", 10, 20),
        Item("Aged Brie", 2, 0),
        Item("Elixir of the Mongoose", 5, 7),
        Item("Sulfuras, Hand of Ragnaros", 0, 80),
        Item("Sulfuras, Hand of Ragnaros", -1, 80),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Item("Conjured Mana Cake", 3, 6)
        ]

    day_count = DayCount()
    gilded_rose = GildedRose(items)
    day_count.attach(gilded_rose)

    for day in range(days):
        day_count.advance_global_day()


update_via_observing(31)
