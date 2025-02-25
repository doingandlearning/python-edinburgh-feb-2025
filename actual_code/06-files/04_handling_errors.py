try:
    with open("not-there.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("File not found!")

# with open("not-there.txt") as file:
#         print(file.read())