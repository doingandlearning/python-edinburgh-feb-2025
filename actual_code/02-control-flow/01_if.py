user_number = 10

if user_number > 10:
    print("That number was too big")

if user_number % 2 == 0:
    print(f"{user_number} was even!")

is_raining = False

if is_raining:
    print("Don't forget your coat!")
else:
    print("Better bring your coat, it's probably going to rain soon!")

favourite_programming_language = "JavaScript"

if favourite_programming_language == "Python":
    print("Do you know any Monty Python sketches?")
elif favourite_programming_language == "TypeScript":
    print("JavaScript is more fun without types")
else:
    print("Why not?")

location = "belfast"

if location.islower():
    print("Don't forget to use capital letters to start proper nouns!")
    # location = location.title()
    print(location.title())
else:
    print(location)

print(location)

is_raining = False
temperature = -2

if is_raining:
    if temperature < 0:
        print("Be careful, it might snow!")
    else:
        print("Don't forget your umbrella")
else:
    print("Lovely day, isn't it!")

if is_raining and temperature < 0:
    print("Be careful, it might snow!")

if is_raining and temperature >= 0:
    print("Don't forget your umbrella!")

if not is_raining:
    print("lovely day isn't it!")


age = 70
is_teenager = None

if age > 12 and age < 20:
    is_teenager = True
else:
    is_teenager = False

print(is_teenager)

is_teenager = True if age > 12 and age < 20 else False
print(is_teenager)