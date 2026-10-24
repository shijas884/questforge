# python
from petterns.creational import CharacterFactory,EnemyBuilder
from domain.items import HealthPotion


# if __name__ == '__main__':

# using Factory

player = CharacterFactory.create('mage','shijas')

# using Builder
boss = (EnemyBuilder("Dragon")
        .with_heath(500)
        .with_attack(50)
        .with_loot(HealthPotion())
        .build()
    )

print(f'create{player.name}(HP:{player.health})')
print(f'create{boss.name}(HP:{boss.health})')












    
  




    

