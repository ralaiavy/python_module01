def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if " VALID" in validation_result:
        return (
            f"Spell recorded: {spell_name} "
            f"({validation_result})"
        )
    return (
        f"Spell '{spell_name}' "
        f"REJECTED! {validation_result}"
    )
