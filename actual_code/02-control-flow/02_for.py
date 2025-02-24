# for num in range(10):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
#
# target = 6
# for num in range(10):
#     if num == target:
#        break
#     print(num)
#
# print("Found the target the number!")

target = 6
for num in range(10):
    if num % 2 == 1:
       continue
    print(num)
