import traceback

def get_valid_number(name, min, max):
    try:
        result = int(input("Give me a number: "))
        if name == "Kevin":
            raise NameError("You have the wrong name!")
        if result < min or result > max:
            raise ValueError("This is out of range")
        raise BufferError()
        return result
    except ValueError as e:  # more specific
        print(e)
        traceback.print_exc()
        return get_valid_number(name, min, max)
    except FileNotFoundError: # less specific
        print("File not found error")
    except OSError:
        print("OSError")


try:
    print(get_valid_number("Angel", 1, 10))
except Exception as e:
    print("Something went wrong")
else:
    print("You got a valid number")
finally:
    print("Have a nice day!")

