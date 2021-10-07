from abs_factory.AbsFactory import AbsFactory
from products.celular.Galaxy import Galaxy
from products.charger.GalaxyCharger import GalaxyCharger


class SamsungFactory(AbsFactory):
    def make_celular(self):
        return Galaxy()

    def make_charger(self):
        return GalaxyCharger()

    def make_phone(self):
        return Galaxy()
