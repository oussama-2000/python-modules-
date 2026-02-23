

def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]

    input = ingredients.strip().split(" ")

    for i in valid:
        if i in input:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
