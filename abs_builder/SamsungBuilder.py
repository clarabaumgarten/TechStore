from abs_builder.AbsBuilder import AbsBuilder
from products.celular.Galaxy import Galaxy
from products.charger.GalaxyCharger import GalaxyCharger
from products.phone.GalaxyPhone import GalaxyPhone


class SamsungBuilder(AbsBuilder):
    def make_basic_box(self):
        celular = Galaxy()
        charger = GalaxyCharger()
        phone = GalaxyPhone()

        self._box.add_item(celular)
        self._box.add_item(charger)
        self._box.add_item(phone)
