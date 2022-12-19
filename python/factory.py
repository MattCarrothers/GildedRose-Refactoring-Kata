from item_classes import *


class Factory:
    def build_item(self, entry):
        if entry[0] == "Aged Brie":
            item = Brie(entry[0], entry[1], entry[2])
        elif entry[0] == "Backstage passes to a TAFKAL80ETC concert":
            item = Backstage(entry[0], entry[1], entry[2])
        elif entry[0] == "Sulfuras, Hand of Ragnaros":
            item = Legendary(entry[0], entry[1], entry[2])
        else:
            item = Basic(entry[0], entry[1], entry[2])
        return item

        # if 'else' in build_item:
        #     print("Sorry Alan.")
