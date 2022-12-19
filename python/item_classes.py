from Interface import implements
from item_interface import Item


class Backstage(implements(Item)):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def adjust_quality(self):
        self.increase_quality_by_(1)
        if self.sell_in < 11:
            self.increase_quality_by_(1)
        if self.sell_in < 6:
            self.increase_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.quality = 0

    def increase_quality_by_(self, num):
        if self.quality < 50:
            self.quality = self.quality + num

    def decrease_quality_by_(self, num):
        if self.quality > 0:
            self.quality = self.quality - num

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class Basic(implements(Item)):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

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


class Brie(implements(Item)):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def adjust_quality(self):
        self.increase_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.increase_quality_by_(1)

    def increase_quality_by_(self, num):
        if self.quality < 50:
            self.quality = self.quality + num

    def decrease_quality_by_(self, num):
        if self.quality > 0:
            self.quality = self.quality - num

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class Legendary(implements(Item)):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def adjust_quality(self):
        return

    def check_out_of_date(self):
        return

    def increase_quality_by_(self, num):
        return

    def decrease_quality_by_(self, num):
        return

    def advance_day(self):
        return
