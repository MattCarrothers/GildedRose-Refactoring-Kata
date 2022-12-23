from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class DayCount(Subject):
    _state = 0
    _observers = []

    def attach(self, observer) -> None:
        self._observers.append(observer)
        print(f"Subject: Attached an observer {observer}.")

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print(f"Day {self._state}: Notifying observers...")
        for observer in self._observers:
            observer.update_quality()
            observer.update_string_to_return_with_current_day(self._state)

    def advance_global_day(self) -> None:
        self._state += 1
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update_quality(self) -> None:
        pass

    @abstractmethod
    def update_string_to_return_with_current_day(self, day):
        pass

