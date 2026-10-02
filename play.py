# python
from domain.classes import Warrior,Mage, Cleric

if __name__ == '__main__':

    warrior = Warrior('Bram')

    mage = Mage('Syllsa')

    warrior.attack(mage)
    mage.special_ability(warrior)
    print(f"Bram HP: {warrior.health}, Sylla HP: {mage.health}")



    cleric = Cleric('cleric')
    print(warrior.health)
    cleric.special_ability(warrior)
    print(warrior.health)
    

