from products.celular.Celular import Celular


class Iphone(Celular):
    def __init__(self) -> None:
        self._brand = 'Apple'
        self._price = 5500.00
        self._name = 'Celular Apple'

    def play_music(self):
        print(f"#{self.get_brand()}# ... Abrindo Itunes ...")
        print(f"#{self.get_brand()}# TOCANDO MÚSICA")
        print(f"#{self.get_brand()}# ... Fechando Itunes ...\n")
