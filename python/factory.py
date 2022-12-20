from strategy import *
from item import Item


class Factory:
    def item_with_strategy(self, entry):
        if entry[0] == "Aged Brie":
            strategy = BrieStrategy
        elif entry[0] == "Backstage passes to a TAFKAL80ETC concert":
            strategy = BackstageStrategy
        elif entry[0] == "Sulfuras, Hand of Ragnaros":
            strategy = LegendaryStrategy
        else:
            strategy = BasicStrategy
        return Item(entry[0], entry[1], entry[2], strategy)
