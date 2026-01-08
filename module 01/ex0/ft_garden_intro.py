def ft_garden_intro():
    info = {"name": "Rose", "height": "25cm", "age": "30 days"}
    print("=== Welcome to My Graden ===")
    print("Plant: " + info["name"])
    print("Height: " + info["height"])
    print("Age: " + info["age"] + "\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()

# if __name__ == "__main__": 
# ensures that certain code runs only when the file is executed directly,
#  not when it’s imported.