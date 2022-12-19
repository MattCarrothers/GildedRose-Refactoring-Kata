from __future__ import print_function
from factory import Factory
from gilded_rose import *


def golden_master_to_string(days):
    string_to_return = "OMGHAI!\n"
    factory = Factory()

    inputs = [
        ["+5 Dexterity Vest", 10, 20],
        ["Aged Brie", 2, 0],
        ["Elixir of the Mongoose", 5, 7],
        ["Sulfuras, Hand of Ragnaros", 0, 80],
        ["Sulfuras, Hand of Ragnaros", -1, 80],
        ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
        ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
        ["Backstage passes to a TAFKAL80ETC concert", 5, 49],
        ["Conjured Mana Cake", 3, 6]
        ]

    items = list(map(factory.build_item, inputs))

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
