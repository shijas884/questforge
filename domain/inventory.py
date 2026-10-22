#python
from domain.exceptions import InventoryEmptyError

class Inventory:

    def __init__(self):
        self._items: list=[]


    def add(self, item) -> None:
        self._items.append(item)

    def use(self, index:int, traget) -> str:
        if not self._items or index < 0 or index >= len(self._items):
            raise InventoryEmptyError(
                f'inventory list is Empaty or index is invalid'
            )

        item = self._items.pop(index)
        return item.apply(traget)

    def list_item(self) -> list[str]:
        return [type(i).__name__ for i in self._items]