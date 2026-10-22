"python"

class QuestForgeErrot(Exception):
    # Base class for all domain-specific error in QuestForge.
    pass


class DeadCharacterError(QuestForgeErrot):
    pass


class InsuffcientManaError(QuestForgeErrot):
    pass


class InvalidActionError(QuestForgeErrot):
    pass


class InventoryEmptyError(QuestForgeErrot):
    pass