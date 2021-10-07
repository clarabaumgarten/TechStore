from abs_factory.AbsFactory import AbsFactory
from products.celular.Iphone import Iphone
from products.charger.IphoneCharger import IphoneCharger


class AppleFactory(AbsFactory):
    def make_celular(self):
        return Iphone()

    def make_charger(self):
        return IphoneCharger()

    def make_phone(self):
        return Iphone()
