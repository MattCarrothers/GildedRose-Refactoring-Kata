from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

import item_classes
from item_classes import *


class Context:

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def build_object(self, data) -> object:
        return self._strategy.create_item(data)


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
