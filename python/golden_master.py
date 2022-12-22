from __future__ import print_function
from gilded_rose import *
from item import Item


def golden_master_to_string(days):
    string_to_return = "OMGHAI!\n"

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

    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        string_to_return += f"-------- day {day} --------\nname, sellIn, quality\n"
        for item in items:
            string_to_return += str(item)
            string_to_return += "\n"
        string_to_return += "\n"
        GildedRose(items).update_quality()
    return string_to_return
