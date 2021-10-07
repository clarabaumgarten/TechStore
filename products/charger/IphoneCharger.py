from products.charger.Charger import Charger


class IphoneCharger(Charger):
    def __init__(self) -> None:
        self._brand = 'Apple'
        self._price = 199.99
        self._name = 'Carregador Apple'
