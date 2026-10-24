from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def apply(self,character) -> str:
    #Apply this item's effect to a character; return a description string
        pass


class Usable(ABC):

    @abstractmethod
    def apply(self,character) -> str:
        # Apply a consumable item's effect
        pass


class Equippable(ABC):

    @abstractmethod
    def equip(self, character) -> str:
        # Equip an item for persistent stat changes
        pass

    