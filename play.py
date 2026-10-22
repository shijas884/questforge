# python
from domain.classes import Warrior,Mage, Cleric,Rogue
from domain.battle import run_special_round,total_party_damage
from domain.character import Character
from domain.items import HealthPotion,Weapon,Armor
from domain.exceptions import QuestForgeErrot



if __name__ == '__main__':

    warrior = Warrior('Bram')

    try:
        warrior.Inventory.use(1,warrior)

    except QuestForgeErrot as e:
        print(f'Action failed:{e}')










    
  




    

