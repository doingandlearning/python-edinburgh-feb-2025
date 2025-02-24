numbers = [1,2,3,4,5]

def double_list(list_of_nums):
    new_numbers = []
    for num in list_of_nums:
        new_numbers.append(num * 2)
    return new_numbers
print(double_list(numbers))


def double(num):
    return num * 2

print(list(map(lambda x: x * 4, numbers)))

square = lambda x: x ** 2
add = lambda a,b: print("Hi")
add(1,2)
def add(a,b):
    return a + b
print(add(1,2))