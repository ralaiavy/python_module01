from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    find: bool = True
    ingredients_lower: str = ingredients.lower()
    for allowed in allowed_ingredients:
        if allowed in ingredients_lower:
            find = True
            break
        find = False

    if find:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
