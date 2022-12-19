from abc import ABC


class Item(ABC):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def adjust_quality(self):
        pass

    def check_out_of_date(self):
        pass

    def increase_quality_by_(self, num):
        if self.quality < 50:
            self.quality = self.quality + num

    def decrease_quality_by_(self, num):
        if self.quality > 0:
            self.quality = self.quality - num

    def advance_day(self):
        pass
