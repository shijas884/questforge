# python
from petterns.singleton import GameManager

def manager1():
    return GameManager()

def manager2():
    return GameManager()


print(id(manager1()))
print(id(manager2()))

print(manager1() is manager2())





    
  




    

