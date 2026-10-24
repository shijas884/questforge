# QuestForge — SOLID Refactor Notes

## S — Single Responsibility Principle

**Meaning:** A class should have one main responsibility.

**QuestForge example:** The `Character` class manages character data and combat behavior. It should not also be responsible for displaying messages to the player.

**Before:**
```python
def attack(self, target):
    target.take_damage(10)
    print(f"{self.name} attacks!")
```

**After:**
```python
def attack(self, target):
    target.take_damage(10)
    return f"{self.name} attacks!"
```

**Explanation:** The character handles the attack and returns a message. The `play.py` file displays that message. If we later change how messages are displayed, we do not need to change the character's combat logic.

**Remember:** One class, one main responsibility.

## O — Open/Closed Principle

**Meaning:** Existing code should be open for extension but closed for unnecessary modification.

**QuestForge example:** We may add new character types, such as an Archer, without repeatedly changing the battle engine.

**Before:**
```python
if character_type == "warrior":
    character.special_ability()
elif character_type == "wizard":
    character.special_ability()
```

**After:**
```python
character.special_ability()
```

**Explanation:** Each character implements its own `special_ability()` method. The battle engine calls that method without checking the character's type. Adding another character becomes easier.

**Remember:** Add new behavior without repeatedly changing existing logic.

## L — Liskov Substitution Principle

**Meaning:** A child class should behave as expected wherever its parent class is used.

**QuestForge example:** `Warrior` and `Wizard` inherit from `Character`. Both should follow the expected rules for taking damage and healing.

**Example:**
```python
def take_damage(self, amount):
    if amount > 0:
        self.health = max(0, self.health - amount)
```

**Explanation:** Taking positive damage should reduce health, and health should not fall below zero. A subclass should not unexpectedly reverse this behavior. Otherwise, the battle engine may behave incorrectly for that character.

**Remember:** Child classes must respect the parent's expected behavior.

## I — Interface Segregation Principle

**Meaning:** A class should not be forced to implement methods it does not need.

**QuestForge example:** A potion may need an `apply()` method, while a weapon may need an `equip()` method.

**Before:**
```python
class Item:
    def apply(self, character):
        pass

    def equip(self, character):
        pass
```

**After:**
```python
from abc import ABC, abstractmethod

class Usable(ABC):
    @abstractmethod
    def apply(self, character):
        pass


class Equippable(ABC):
    @abstractmethod
    def equip(self, character):
        pass
```

**Explanation:** A potion can implement `Usable`, and a weapon can implement `Equippable`. Neither item needs to provide an irrelevant method.

This is a possible refactor for QuestForge if your current item design requires every item to implement both methods.

**Remember:** Keep interfaces focused on the behavior an object actually needs.

## D — Dependency Inversion Principle

**Meaning:** High-level game logic should depend on an abstraction rather than directly on a specific implementation.

**QuestForge example:** Imagine `GameService` needs to save game progress. It should not have to know the details of saving to a particular file.

**Before:**
```python
class GameService:
    def __init__(self):
        self.saver = FileSaver()
```

**After:**
```python
class GameService:
    def __init__(self, saver):
        self.saver = saver
```

**Explanation:** `GameService` receives its saver from outside instead of creating a specific saver itself. We can supply different compatible saving implementations without rewriting the game service.

This is an illustrative example. Apply it if your project has saving logic or another dependency that is tightly coupled to a concrete class.

**Remember:** Receive dependencies from outside when that makes the code easier to change and test.

## Final Summary

- **S — Single Responsibility:** Keep each class focused on one main job.
- **O — Open/Closed:** Make adding new character behavior easier.
- **L — Liskov Substitution:** Preserve expected behavior in subclasses.
- **I — Interface Segregation:** Avoid forcing objects to implement irrelevant methods.
- **D — Dependency Inversion:** Reduce tight coupling to concrete implementations.

