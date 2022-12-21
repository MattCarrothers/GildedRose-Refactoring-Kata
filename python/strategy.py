from __future__ import annotations
from abc import ABC


class Strategy(ABC):

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


class BackstageStrategy(Strategy):
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


class BrieStrategy(Strategy):
    def adjust_quality(self):
        self.increase_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.increase_quality_by_(1)

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class LegendaryStrategy(Strategy):
    def increase_quality_by_(self, num):
        pass

    def decrease_quality_by_(self, num):
        pass


class BasicStrategy(Strategy):
    def adjust_quality(self):
        self.decrease_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.decrease_quality_by_(1)

    def advance_day(self):
        self.sell_in = self.sell_in - 1
