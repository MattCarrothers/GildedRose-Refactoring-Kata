from factory_strategy import FactoryStrategy


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.strategy = None

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_item(self):
        factory = FactoryStrategy()
        self.get_strategy(factory)
        self.strategy.adjust_quality(self)
        self.strategy.advance_day(self)
        self.strategy.check_out_of_date(self)

    def increase_quality_by_(self, num):
        self.strategy.increase_quality_by_(self, num)

    def decrease_quality_by_(self, num):
        self.strategy.decrease_quality_by_(self, num)

    def get_strategy(self, factory):
        self.strategy = factory.get_strategy(self)

