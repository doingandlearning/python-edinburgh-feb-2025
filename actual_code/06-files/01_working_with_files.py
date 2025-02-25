file = open("file.txt")  # this is a file handle!

print(file.read())  # whole file!

file.seek(0)

lines = [line.strip() for line in file.readlines()] # open the whole the file but as a list of lines!

for line in lines:
    print(line.upper())
print(["     This is a file\n    ".strip()])

file.seek(0)

# current_line = file.readline()
# walrus operator
while current_line := file.readline():
    print(current_line)

file.seek(0)

current_line = file.readline()
while current_line:
    print(current_line)
    current_line = file.readline()

file.close()