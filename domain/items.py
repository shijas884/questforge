from domain.item import Item

class HealthPotion(Item):
    def __init__(self, heal_amount:int = 25):

        self.heal_amount = heal_amount


    def apply(self, character) -> str:
        character.heal(self.heal_amount)
        return f'{character.name} drinks a potion and heal {self.heal_amount} HP! '


class Weapon(Item):
    def __init__(self, name: str, bonus_attack: int):
        self.name = name
        self.bonus_attack = bonus_attack


    def apply(self, character) -> str:
        character.attack_power += self.bonus_attack
        return f"{character.name} equips {self.name} (+{self.bonus_attack} ATK)"

class Armor(Item):

    def __init__(self, name: str, defense: int):
        if defense < 0:
            raise ValueError('Defense cannot be negative')

        self.name = name
        self.defense = defense

    def apply(self, character) -> str:

        character.set_defense(character.defense + self.defense)
        return f'{character.name} equips {self.name} (+ {self.defense} DEF)'





       
        
    