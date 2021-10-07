from abc import ABC, abstractmethod


class Phone(ABC):
    def listening(self):
        print(f'#{self.get_brand()}#: Escutando\n')

    def get_price(self):
        return self._price
    
    def get_brand(self):
        return self._brand
    
    def get_name(self):
        return self._name
