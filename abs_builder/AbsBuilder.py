from abc import ABC, abstractmethod
from products.box.Box import Box


class AbsBuilder(ABC):
    _box = Box()

    @abstractmethod
    def make_basic_box():
        pass

    def get_box(self):
        return self._box
    
    def reset(self):
        self._box.reset()
