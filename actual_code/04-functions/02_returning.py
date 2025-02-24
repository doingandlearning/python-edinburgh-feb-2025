def shout_message(message: str):
    return message.upper()


print(shout_message("How are you?"))

def square(n: float):
    return n * n

def add_four(n: float | int):
    return n + 4

print(add_four(square(4.0)))

# user = float(input("Give me a number: "))
# if square(user) > 100:
#     print("Wow! That was a big number!")
#
# print(f"100 squared is {square(100):,}")
#
# print(f"{'Edinburgh is great':^100}")

def age_and_name(user):
    return user["age"], user["name"]

user_object = {
    "name": "Ethan",
    "age": 12,
    "interests": ["Speed cubing"]
}

age, name = age_and_name(user_object)

print(f"{name} is {age} years old.")