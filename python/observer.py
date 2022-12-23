from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class DayCount(Subject):
    _state = -1
    _observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        print(f"Subject: Attached an observer {observer}.")

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print(f"Day {self._state}: Notifying observers...")
        for observer in self._observers:
            observer.update_output_string(self._state)
            observer.update_quality()


    def advance_global_day(self) -> None:
        self._state += 1
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update_quality(self) -> None:
        pass

    @abstractmethod
    def update_output_string(self, day):
        pass

