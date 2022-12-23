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
    _state = 0
    _observers = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        string_to_return = ""
        for observer in self._observers:
            string_to_return += f"-------- day {self._state} --------\nname, sellIn, quality\n"
            for item in observer.items:
                string_to_return += str(item)
                string_to_return += "\n"
            string_to_return += "\n"
            observer.update_quality()
        print(string_to_return)

    def advance_global_day(self) -> None:
        self._state += 1
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update_quality(self, subject: Subject) -> None:
        pass
