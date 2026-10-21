# python
from domain.classes import Warrior,Mage, Cleric,Rogue
from domain.battle import run_special_round,total_party_damage
from domain.character import Character
from domain.items import HealthPotion,Weapon,Armor

def main():

    warrior = Warrior('warrior')

    potion1 = HealthPotion()
    potion2 = HealthPotion()
    weapon = Weapon('iron sword', bonus_attack=10)

    warrior.Inventory.add(potion1)
    warrior.Inventory.add(potion2)
    warrior.Inventory.add(weapon)

    print(warrior.Inventory.use(0,warrior))
    print(warrior.Inventory.use(0,warrior))
    print(warrior.Inventory.use(0,warrior))


    print(warrior.attack_power)





    

if __name__ == '__main__':

    main()    




    
  




    

