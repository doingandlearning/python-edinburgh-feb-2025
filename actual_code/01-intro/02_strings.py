example_string = "This is an example string"
#                 0
print(example_string.find("banana"))

# print(example_string.replace("example", "banana"))

print(example_string.center(100))

name ="Angel"

print("Hello " + name + ", how are you?" + str(1 + 1))
print(f"Hello {name}, how are you?")  # `${}`
print(f"Hello {name}, how are you? {1 + 1 }")  # `${}`
print("Hello {}, how are you?".format(name))