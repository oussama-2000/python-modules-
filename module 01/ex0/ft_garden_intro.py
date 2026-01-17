def ft_garden_intro() -> None:
    """shows plant informations"""

    info = {"name": "Rose", "height": "25cm", "age": "30 days"}
    print("=== Welcome to My Graden ===")
    print("Plant: " + info["name"])
    print("Height: " + info["height"])
    print("Age: " + info["age"] + "\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
