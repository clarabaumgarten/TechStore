import operator
import functools


class Box:
    _box = []

    def add_item(self, item):
        self._box.append(item)

    def total_price(self):
        item_price = map(lambda item: item.get_price(), self._box)
        return functools.reduce(operator.add, item_price)
    
    def items_in_box(self):
        print("Contem:")
        for item in self._box:
            print(f"- {item.get_name()}, {item.get_price()}")
        print("")
    
    def reset(self):
        self._box = []