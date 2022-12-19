from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

import item_classes
from item_classes import *


class Context:

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):

    @abstractmethod
    def create_item(self, data: List):
        pass


class BackstageStrategy(Strategy):
    def create_item(self, data: List) -> item_classes.Backstage:
        return Backstage(data[0], data[1], data[2])


class BrieStrategy(Strategy):
    def create_item(self, data: List) -> item_classes.Brie:
        return Brie(data[0], data[1], data[2])


class LegendaryStrategy(Strategy):
    def create_item(self, data: List) -> item_classes.Legendary:
        return Legendary(data[0], data[1], data[2])


class BasicStrategy(Strategy):
    def create_item(self, data: List) -> item_classes.Basic:
        return Basic(data[0], data[1], data[2])
