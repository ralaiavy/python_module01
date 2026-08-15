from typing import cast

from ex0 import Creature, CreatureFactory
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    base = factory.create_base()
    _describe_attack_heal(base)

    print(" evolved:")
    evolved = factory.create_evolved()
    _describe_attack_heal(evolved)


def _describe_attack_heal(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(cast(HealCapability, creature).heal())


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")

    print(" base:")
    base = factory.create_base()
    _describe_attack_transform_attack_revert(base)

    print(" evolved:")
    evolved = factory.create_evolved()
    _describe_attack_transform_attack_revert(evolved)


def _describe_attack_transform_attack_revert(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    transformer = cast(TransformCapability, creature)
    print(transformer.transform())
    print(creature.attack())
    print(transformer.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    test_healing(healing_factory)
    print()

    transform_factory = TransformCreatureFactory()
    test_transform(transform_factory)


if __name__ == "__main__":
    main()
