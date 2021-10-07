from abc import ABC, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def make_celular(self):
        pass

    @abstractmethod
    def make_charger(self):
        pass

    @abstractmethod
    def make_phone(self):
        pass
