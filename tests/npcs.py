import abc


class AbstractFriendlyNPC(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def interact(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class HealerNPC(AbstractFriendlyNPC):
    def __init__(self) -> None:
        self.name = "Guen the Healer"

    def interact(self) -> int:
        print(f"You've been healed by {self.name}.... for 40 HP!")
        return 40

    def __str__(self) -> str:
        return self.name


class MysticMerchant(AbstractFriendlyNPC):
    def __init__(self) -> None:
        self.name = "Eldric the Mystic Merchant"

    def interact(self) -> int:
        print(f"Welcome to my shop, I have many wares for sale. Take this treasue key for free!")
        return 0

    def __str__(self) -> str:
        return self.name
