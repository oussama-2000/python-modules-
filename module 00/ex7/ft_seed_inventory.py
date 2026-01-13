def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    units_status = {
                    "packets": "packets available",
                    "grams": "grams total",
                    "area": f"covers {quantity} square meters",
                    "unknown": "Unknown unit type"
                    }

    if unit not in ("packets", "grams", "area"):
        unit = "unknown"
    status = units_status[unit]
    qu = quantity if unit != "area" else ""
    if unit != "unknown":
        print(f"{seed_type.capitalize()} seeds : {qu} {status}")
    else:
        print(status)
