from item_interface import Item


class Backstage(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def adjust_quality(self):
        self.increase_quality_by_(1)
        if self.sell_in < 11:
            self.increase_quality_by_(1)
        if self.sell_in < 6:
            self.increase_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.quality = 0

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class Basic(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def adjust_quality(self):
        self.decrease_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.decrease_quality_by_(1)

    def increase_quality_by_(self, num):
        if self.quality < 50:
            self.quality = self.quality + num

    def decrease_quality_by_(self, num):
        if self.quality > 0:
            self.quality = self.quality - num

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class Brie(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def adjust_quality(self):
        self.increase_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.increase_quality_by_(1)

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class Legendary(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def increase_quality_by_(self, num):
        return

    def decrease_quality_by_(self, num):
        return
