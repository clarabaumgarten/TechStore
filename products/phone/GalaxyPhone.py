from products.phone.Phone import Phone


class GalaxyPhone(Phone):
    def __init__(self) -> None:
        self._brand = 'Samsung'
        self._price = 90.00
        self._name = 'Fone Samsung'
