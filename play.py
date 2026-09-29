# python
from domain.character import Character

if __name__ == '__main__':

    hero = Character("Aria",100,15)
    goblin = Character("Goblin",30,5)

    print(hero.describe())
    print(goblin.describe())

    hero.attack(goblin)
    print(goblin.describe())

    goblin.attack(hero)
    print(hero.describe())

    hero.attack(goblin)
    print(goblin.describe())

    goblin.attack(hero)
    print(hero.describe())

    hero.attack(goblin)
    print(goblin.describe())

    goblin.attack(hero)
    print(hero.describe())


    goblin.heal(40)
    print(goblin.describe())

    warrior = Character("warrior",80,10)
    dragon = Character("dragon",100,20)


