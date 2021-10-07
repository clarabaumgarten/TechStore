from products.celular.Iphone import Iphone
from products.celular.Galaxy import Galaxy
from abs_factory.AppleFactory import AppleFactory


galaxy = Galaxy()
galaxy.call('Mamys')
galaxy.play_music()
galaxy.text('amigaa, ta ai?', 'mari')

iphone = Iphone()
iphone.call('Mamys')
iphone.play_music()
iphone.text('amigaa, ta ai?', 'mari')
