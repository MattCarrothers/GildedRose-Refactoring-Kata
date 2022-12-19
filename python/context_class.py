from __future__ import annotations
from abc import ABC


class Context:

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def adjust_quality(self):
        return self._strategy.adjust_quality()

    def check_out_of_date(self):
        return self._strategy.check_out_of_date()

    def increase_quality_by_(self, num):
        return self._strategy.increase_quality_by_(num)

    def decrease_quality_by_(self, num):
        return self._strategy.decrease_quality_by_(num)

    def advance_day(self):
        return self._strategy.advance_day()


class Strategy(ABC):

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


class BackstageStrategy(Strategy):
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


class BrieStrategy(Strategy):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def adjust_quality(self):
        self.increase_quality_by_(1)

    def check_out_of_date(self):
        if self.sell_in < 0:
            self.increase_quality_by_(1)

    def advance_day(self):
        self.sell_in = self.sell_in - 1


class LegendaryStrategy(Strategy):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def increase_quality_by_(self, num):
        pass

    def decrease_quality_by_(self, num):
        pass


class BasicStrategy(Strategy):
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
