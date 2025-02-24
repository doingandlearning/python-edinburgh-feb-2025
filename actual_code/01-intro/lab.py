import sys

print(sys.argv)

number_1 = float(sys.argv[1])
number_2 = float(sys.argv[2])

print(f"Sum: {number_1 + number_2}")
print(f"Dividend: {number_1 / number_2}")
print(f"Difference: {number_1 - number_2}")
print(f"Product: {number_1 * number_2}")

