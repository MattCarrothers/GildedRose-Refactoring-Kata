from item_classes import *


class Factory:
    def __init__(self, entries):
        self.entries = entries
        self.items = []

    def build_items(self):
        for entry in self.entries:
            if entry[0] == "Aged Brie":
                item = Brie(entry[0], entry[1], entry[2])
            elif entry[0] == "Backstage passes to a TAFKAL80ETC concert":
                item = Backstage(entry[0], entry[1], entry[2])
            elif entry[0] == "Sulfuras, Hand of Ragnaros":
                item = Legendary(entry[0], entry[1], entry[2])
            else:
                item = Basic(entry[0], entry[1], entry[2])
            self.items.append(item)
