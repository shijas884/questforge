from domain.character import Character


class CharacterBuff(Character):
    # Base decorator: Wraps a Charater and delegates by defult.
    def __init__(self, wrapped:Character):
        # We don't call super().__init__because we are Wrappong,
        # not subclassing the state

        self._wrapped = wrapped

    def __getattr__(self, name):
       # Delegate any attribute/method not explicitly overridden
       #  to the wrapped object
       
       return getattr(self._wrapped, name)

    @property
    def attack_power(self):
        return self._wrapped.attack_power

    def special_ability(self, target):
        return self._wrapped.special_ability(target)


class RageBuff(CharacterBuff):

    @property
    def attack_power(self):
        # Apply the 50% increase to whatever the underlying attack
        #  power is 

        return int(self._wrapped.attack_power *1.5)

    def __repr__(self):
        return f'Raging({self._wrapped.name})'


class PoisonDebuff(CharacterBuff):

    def __init__(self, wrapped: Character, damage_per_turn: int = 5):
        super().__init__(wrapped)
        self.damage_per_turn = damage_per_turn

    def tick(self) -> str:
        self._wrapped.take_damage(self.damage_per_turn)
        return f'''{self._wrapped.name} takes {self.damage_per_turn} poison damage!'''


    

    

        