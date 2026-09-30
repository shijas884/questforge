# python
from domain.character import Character

if __name__ == '__main__':

    hero = Character("Aria",100,15)
    shijas = Character("shijas",100,15)

    hero.attack(shijas)
    shijas.heal(100)

    print(shijas.health)

    

 



