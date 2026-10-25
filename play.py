# python
from petterns.singleton import GameManager

# Get the manager and set some state
manager1 = GameManager()
manager1.difficulty = 'hard'

# Somewhere else in the code, we try to create a new manager 
manager2 = GameManager()


print(f'manger-2 diffcuty: {manager2.difficulty}')
# out put 'hard'  because manager1 and manager2 are exact same object

print(f'are they the same objects? {manager1 is manager2}')










    
  




    

