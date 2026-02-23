import alchemy

# print(alchemy.__dict__) # package object package namespace

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")

    print("alchemy.elements.create_fire(): ", end="")
    try:
        fire = alchemy.elements.create_fire()
        print(fire)
    except AttributeError as e:
        print(e)

    print("alchemy.elements.create_water(): ", end="")
    try:
        water = alchemy.elements.create_water()
        print(water)
    except AttributeError as e:
        print(e)

    print("alchemy.elements.create_earth(): ", end="")
    try:
        earth = alchemy.elements.create_earth()
        print(earth)
    except AttributeError as e:
        print(e)

    print("alchemy.elements.create_air(): ", end="")
    try:
        air = alchemy.elements.create_air()
        print(air)
    except AttributeError as e:
        print(e)

    print("\nTesting package-level access (controlled by __init__.py):")

    print("alchemy.create_fire(): ", end="")
    try:
        fire2 = alchemy.create_fire()
        print(fire2)
    except AttributeError as e:
        print(f"{e.__class__.__name__} - not exposed")

    print("alchemy.create_water(): ", end="")
    try:
        water2 = alchemy.create_water()
        print(water2)
    except AttributeError as e:
        print(f"{e.__class__.__name__} - not exposed")

    print("alchemy.create_earth(): ", end="")
    try:
        earth2 = alchemy.create_earth()
        print(earth2)
    except AttributeError as e:
        print(f"{e.__class__.__name__} - not exposed")

    print("alchemy.create_air(): ", end="")
    try:
        air2 = alchemy.create_air()
        print(air2)
    except AttributeError as e:
        print(f"{e.__class__.__name__} - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
