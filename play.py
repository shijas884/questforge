# python
from domain.classes import Warrior
from petterns.decorators import RageBuff, PoisonDebuff


hero = Warrior('Bram')
print(f'Base attack:{hero.attack_power}')


# Wrap the hero in a Ragebuff
raging_hero = RageBuff(hero)
print(f'Raging attack:{raging_hero.attack_power}')

# Wrap the raging in a posonDebuff(Stacking!)
poisoned_raging_hero = PoisonDebuff(raging_hero)
print(f"Still raging attack: {poisoned_raging_hero.attack_power}")


# Trigger the poison
print(poisoned_raging_hero.tick())
print(f"HP after poison: {poisoned_raging_hero.health}")

    
  




    

