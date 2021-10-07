from abc import ABC, abstractmethod


class Celular(ABC):
    def call(self, someone):
        print(f'#{self.get_brand()}#: Ligando para {someone}\n')

    def text(self, message, someone):
        print(f'#{self.get_brand()}#: Para: {someone}')
        print(f'#{self.get_brand()}#: Mensagem: {message}\n')

    @abstractmethod
    def play_music():
        pass

    def get_price(self):
        return self._price

    def get_brand(self):
        return self._brand
    
    def get_name(self):
        return self._name
