from abs_factory.AppleFactory import AppleFactory
from abs_factory.SamsungFactory import SamsungFactory


samsung = SamsungFactory()

samsung_celular = samsung.make_celular()
samsung_celular.call('Mamys')
samsung_celular.play_music()
samsung_celular.text('amigaa, ta ai?', 'mari')

samsung_charger = samsung.make_charger()
samsung_charger.charge()


apple = AppleFactory()

apple_celular = apple.make_celular()
apple_celular.call('Mamys')
apple_celular.play_music()
apple_celular.text('amigaa, ta ai?', 'mari')

apple_charger = apple.make_charger()
apple_charger.charge()
