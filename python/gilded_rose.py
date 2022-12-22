from factory_strategy import FactoryStrategy


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        strategy_factory = FactoryStrategy()
        [item.update_item(strategy_factory) for item in self.items]
