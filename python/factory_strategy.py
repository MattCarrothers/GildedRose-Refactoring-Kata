from strategy import *


class FactoryStrategy:
    def get_strategy(self, item):

        if item.name == "Aged Brie":
            strategy = BrieStrategy
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            strategy = BackstageStrategy
        elif item.name == "Sulfuras, Hand of Ragnaros":
            strategy = LegendaryStrategy
        else:
            strategy = BasicStrategy
        return strategy
