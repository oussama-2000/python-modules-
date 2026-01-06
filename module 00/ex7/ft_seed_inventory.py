# type hints not forced 
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    units_status = {"packets": "packets available", "grams": "grams total",
                    "area": "covers X square meters",
                    "unknown": "Unknown unit type"}

    if unit not in ("packets", "grams", "area"):
        unit = "unknown"
    status = units_status[unit]
    print(f"{seed_type.capitalize()} seeds : {quantity} {status}")
