# python
from domain.classes import Warrior,Mage, Cleric,Rogue
from domain.battle import run_special_round,total_party_damage

if __name__ == '__main__':

    party = [Warrior("Bram"), Mage("Sylla"), Rogue("Kade")]
    cleric = Cleric('cleric')
    total_party_damage(party,cleric)
    print(cleric.health)



