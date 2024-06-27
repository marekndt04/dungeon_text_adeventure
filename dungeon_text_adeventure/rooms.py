import abc


class AbstractRoom(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def enter(self) -> str:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class SimpleRoom(AbstractRoom):
    def __init__(self) -> None:
        self.name = "Modest Chambers"

    def enter(self) -> str:
        return f"You have entered {self.name}."

    def __str__(self) -> str:
        return self.name


class MonsterRoom(AbstractRoom):
    def __init__(self) -> None:
        self.name = "Monster Room"

    def enter(self) -> str:
        return f"You have entered {self.name}."

    def __str__(self) -> str:
        return self.name


class TreasureRoom(AbstractRoom):
    def __init__(self) -> None:
        self.name = "Treasure Room"

    def enter(self) -> str:
        return f"You have entered {self.name}."

    def __str__(self) -> str:
        return self.name
