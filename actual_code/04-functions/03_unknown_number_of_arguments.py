def add(a, b):
    return a + b

print(add(2,3))

def add_three_things(a,b,c):
    return a + b + c

print(add_three_things(1,2,3))

def add(*nums):  # function add(...nums)
    print(nums)
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3))
print(add(1,2,3,4))
print(add(1,2,3,4,5))

# Andrew says the total is ___

def counter_and_total(counter, *nums ):
    total = 0
    for num in nums:
        total += num
    return f"{counter} says the total is {total}"

print(counter_and_total( "Andrew", 1,2,23))

numbers = (1,2,3,4,5)

print(add(*numbers))