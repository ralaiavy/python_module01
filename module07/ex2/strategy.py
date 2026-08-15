from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        transformer = cast(TransformCapability, creature)
        print(transformer.transform())
        print(creature.attack())
        print(transformer.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        print(creature.attack())
        healer = cast(HealCapability, creature)
        print(healer.heal())
