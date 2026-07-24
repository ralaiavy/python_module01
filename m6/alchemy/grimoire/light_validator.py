def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients = light_spell_allowed_ingredients()
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
