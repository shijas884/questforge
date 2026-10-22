# python
from domain.classes import Warrior,Mage, Cleric,Rogue
from domain.battle import run_special_round,total_party_damage
from domain.character import Character
from domain.items import HealthPotion,Weapon,Armor
from domain.exceptions import QuestForgeErrot


if __name__ == '__main__':


    mana = Mage('Sylla')
    warrior = Warrior('Bram')

    try:
        # sylla strat 50 mana. 3 fireballs(20 cost each) will fail

        mana.special_ability(warrior)
        mana.special_ability(warrior)
        mana.special_ability(warrior)

    except QuestForgeErrot as e:
        print(e)





    
  




    

