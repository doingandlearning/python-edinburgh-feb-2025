empty_list = []  # list()
print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo", "John"]

print(beatles[::-1])
print(beatles[0])
print(beatles[0:2])

print(beatles.append("Mark")) # add a single element
print(beatles)

beatles.extend(("Gillian", "Chong"))

print(beatles)

while "John" in beatles:
    beatles.remove("John")
print(beatles)

beatles.insert(2, "Stephen")
print(beatles)

for member in beatles:
    print(f"{member} is in the Beatles")

beatles.clear()
print(beatles)

nested_list = [True, [1,2,3], ["one", ["two", "three"]]]

print(nested_list[2][1][0])