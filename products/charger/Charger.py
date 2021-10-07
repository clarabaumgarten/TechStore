from abc import ABC, abstractmethod


class Charger(ABC):
    def charge(self):
        print(f'#{self.get_brand()}#: Plugando carregador no celular\n')
        print(f'#{self.get_brand()}#: Carregando...\n')
    
    def get_price(self):
        return self._price

    def get_brand(self):
        return self._brand
    
    def get_name(self):
        return self._name
