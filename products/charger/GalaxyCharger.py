from products.charger.Charger import Charger


class GalaxyCharger(Charger):
    def __init__(self) -> None:
        self._brand = 'Samsung'
        self._price = 59.99
        self._name = 'Carregador Samsung'
