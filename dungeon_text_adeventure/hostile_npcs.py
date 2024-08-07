import abc


class AbstractHostileNPC(abc.ABC):
    def __init__(self) -> None:
        self.health = 0

    @abc.abstractmethod
    def attack(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


class Dragon(AbstractHostileNPC):
    def __init__(self) -> None:
        self.health = 25

    def attack(self) -> int:
        return 20

    def __str__(self) -> str:
        return "The Dragon, eater of worlds"


class Troll(AbstractHostileNPC):
    def __init__(self) -> None:
        self.health = 20

    def attack(self) -> int:
        return 10

    def __str__(self) -> str:
        return "The Troll, destroyer of dreams"


class LesserDemon(AbstractHostileNPC):
    def __init__(self) -> None:
        self.health = 15

    def attack(self) -> int:
        return 10

    def __str__(self) -> str:
        return "The Lesser Demon, a harbinger of chaos"
