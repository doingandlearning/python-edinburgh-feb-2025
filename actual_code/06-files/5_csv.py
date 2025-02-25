import csv

with open("samples.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Character Limit", "Kate Conger and Ryan Mac"])
    writer.writerow(["Lord of Emperors", "Guy Gavriel Kay"])
    writer.writerow(["Before They Were Hanged", "Joe Abercrombie"])

with open("samples.csv", "w") as file:
    headers = ["Title", "Author"]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerow({"Title": "Character Limit", "Author": "Kate Conger and Ryan Mac"})
    writer.writerow({"Title": "Lord of Emperors", "Author": "Guy Gavriel Kay"})

with open("samples.csv") as file:
   reader = csv.DictReader(file)
   for row in reader:
       print(row)


import json
# json.loads(file)
print(json.dumps(["1", True, "Hello"]))  # Turns Python objects into a JSON string
print(json.loads('["1", true, "Hello"]')) # Turns a JSON string into a Python object