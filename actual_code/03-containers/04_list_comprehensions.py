list_of_numbers = []

for num in range(100):
    if num % 2 == 0:
        list_of_numbers.append(num)

print(list_of_numbers)

alternative = [num
               for num in range(100)
               if num % 2 == 0
               ]  # list comprehensions
print(alternative)