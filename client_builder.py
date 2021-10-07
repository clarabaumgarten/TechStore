from abs_builder.AppleBuilder import AppleBuilder
from abs_builder.SamsungBuilder import SamsungBuilder


apple = AppleBuilder()
apple.make_basic_box()
box = apple.get_box()
box.items_in_box()
print('Total da compra: ', box.total_price(), '\n')

box.reset()
samsung = SamsungBuilder()
samsung.make_basic_box()
box = samsung.get_box()
box.items_in_box()
print('Total da compra: ', box.total_price())
