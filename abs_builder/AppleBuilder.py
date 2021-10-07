from abs_builder.AbsBuilder import AbsBuilder
from products.celular.Iphone import Iphone
from products.charger.IphoneCharger import IphoneCharger
from products.phone.IphonePhone import IphonePhone


class AppleBuilder(AbsBuilder):
    def make_basic_box(self):
        celular = Iphone()
        charger = IphoneCharger()
        phone = IphonePhone()

        self._box.add_item(celular)
        self._box.add_item(charger)
        self._box.add_item(phone)
