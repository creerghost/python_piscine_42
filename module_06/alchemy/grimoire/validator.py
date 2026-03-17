def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    if any(elem in ingredients.lower() for elem in valid_elements):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
