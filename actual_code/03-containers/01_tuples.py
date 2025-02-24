empty_tuple = tuple() # or just ()

print(empty_tuple)
print(type(empty_tuple))

tuple1 = (1,3,5,7,9,1,1,1)

print(tuple1.count(0))
print(tuple1.index(1))

print(tuple1[4])
print(tuple1[1:4])
print(tuple1[1:4:2])
print(tuple1[:4])
print(tuple1[::2])
print(tuple1[::-1])

print(len(tuple1))

element = 3
if element in tuple1:
    print(f"Element {element} at position {tuple1.index(element)}")
else:
    print("Element not in tuple!")

for num in tuple1:
    print(num)

tuple2 = ("Natalia", "Angel")

first, second = tuple2

print(first)
print(second)