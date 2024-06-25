import abc


class AbstractClass(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def attack(self) -> int:
        pass

    @abc.abstractmethod
    def take_damage(self, damage: int) -> None:
        pass

    @abc.abstractmethod
    def is_alive(self) -> bool:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class Warrior(AbstractClass):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.health = 100

    def attack(self) -> int:
        return 10

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} the Warrior"


class Mage(AbstractClass):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.health = 50

    def attack(self) -> int:
        return 20

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} the Mage"


class Rogue(AbstractClass):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.health = 75

    def attack(self) -> int:
        return 15

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} the Rogue"
