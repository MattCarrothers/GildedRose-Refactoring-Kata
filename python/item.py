class Item:
    def __init__(self, name, sell_in, quality, strategy):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.strategy = strategy

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def adjust_quality(self):
        return self.strategy.adjust_quality(self)

    def check_out_of_date(self):
        return self.strategy.check_out_of_date(self)

    def increase_quality_by_(self, num):
        return self.strategy.increase_quality_by_(self, num)

    def decrease_quality_by_(self, num):
        return self.strategy.decrease_quality_by_(self, num)

    def advance_day(self):
        return self.strategy.advance_day(self)
