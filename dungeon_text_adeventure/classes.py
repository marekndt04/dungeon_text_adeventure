import abc


class AbstractClass(abc.ABC):
    def __init__(self, name: str, spec: str) -> None:
        self.name = name
        self.spec = spec

    @abc.abstractmethod
    def attack(self, target: str) -> int:
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
    def __init__(self, name: str, spec: str) -> None:
        super().__init__(name, spec)
        self.health = 100

    def attack(self, target: str) -> int:
        return 10

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} the Warrior"


class Mage(AbstractClass):
    def __init__(self, name: str, spec: str) -> None:
        super().__init__(name, spec)
        self.health = 50

    def attack(self, target: str) -> int:
        return 20

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} the Mage"


class Rogue(AbstractClass):
    def __init__(self, name: str, spec: str) -> None:
        super().__init__(name, spec)
        self.health = 75

    def attack(self, target: str) -> int:
        return 15

    def take_damage(self, damage: int) -> None:
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name} the Rogue"