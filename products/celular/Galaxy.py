from products.celular.Celular import Celular


class Galaxy(Celular):
    def __init__(self) -> None:
        self._brand = 'Samsung'
        self._price = 1800.00
        self._name = 'Celular Samsung'

    def play_music(self):
        print(f"#{self.get_brand()}# ... Abrindo Spotify ...")
        print(f"#{self.get_brand()}# TOCANDO MÚSICA")
        print(f"#{self.get_brand()}# ... Fechando Spotify ...\n")
