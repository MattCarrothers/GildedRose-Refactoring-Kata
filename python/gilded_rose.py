from factory_strategy import FactoryStrategy


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        [item.update_item() for item in self.items]
