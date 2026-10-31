# python
from domain.classes import Warrior
from petterns.decorators import RageBuff, PoisonDebuff


hero = Warrior("Bram")
print(f"Base attack: {hero.attack_power}")


# Wrap the hero in a RageBuff
raging_hero = RageBuff(hero)
print(f"Raging attack: {raging_hero.attack_power}")


# Wrap the raging hero in a PoisonDebuff (Stacking!)
poisoned_raging_hero = PoisonDebuff(raging_hero)
print(f"Still raging attack: {poisoned_raging_hero.attack_power}")


# Trigger the poison
print(poisoned_raging_hero.tick())
print(f"HP after poison: {poisoned_raging_hero.health}")

orginal_hero = poisoned_raging_hero._wrapped._wrapped
print(orginal_hero is hero)
print("Original attack:", orginal_hero.attack_power)
print("Original health:", orginal_hero.health)
