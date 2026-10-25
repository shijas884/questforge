# python
class GameManager:
    _instance = None

    def __new__(cls):
        # Override the creation of the object to ensure only one exists
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self):
        # Prevent re-initialization if__init__is called multiple times
        if self._initialized:
            return

        self.party: list = []
        self.turn_count: int = 0
        self.difficulty: str = 'normal'
        self._initialized = True

    def strat_new_session(self, party:list) -> None:
        self.party = party
        self.turn_count = 0 

    def nest_turn(self) -> int:
        self.turn_count += 1
        return self.turn_count
        