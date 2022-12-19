# -*- coding: utf-8 -*-
from __future__ import print_function
from gilded_rose import *
from item_classes import *


def golden_master_print(days):
    print("OMGHAI!")
    items = [
             Basic(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Brie(name="Aged Brie", sell_in=2, quality=0),
             Basic(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Legendary(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Legendary(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Basic(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()


golden_master_print(31)
