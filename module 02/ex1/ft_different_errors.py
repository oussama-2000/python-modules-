

def garden_operations():
    # try:
    #     int(input("enter a number: "))
    #     value = 5 / 0
    #     open(file_name)
    
    options = {
            "1": "value1",
            "2": "value2",
            "3": "value3"
            }
    for o, v in options.items():
        print(f"{o} {v}")
    inp = input("Enter option: ")
    option = options[inp]
    print(f"--- {option} ---")
    if inp == "1":
        height = int(input("Enter an integer: "))
        print(f"your input is : {height}")
    elif inp == "2":
        dividend = int(input("Enter Dividend: "))
        divisor = int(input("Enter Divisor: "))
        division = dividend / divisor
        print(f"{dividend} / {divisor} = {division}")
    elif inp == "3":
        file_name = input("Enter file name: ")
        open(file_name)


def test_error_types():
    try:
        garden_operations()
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Testing ZeroDivisionError..."
              "\nCaught ZeroDivisionError: division by zero")
    except FileNotFoundError as e:
        print("Testing FileNotFoundError...\n"
              f"Caught FileNotFoundError: No such file '{e.filename}'")
    except KeyError as e:
        print("Testing KeyError...\n"
              f"Caught KeyError: {e}")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Testing multiple errors together..."
              "Caught an error, but program continues!")
    print("All error types tested successfully!")
test_error_types()
