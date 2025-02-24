empty_dict = {}  # dict()

print(empty_dict)
print(type(empty_dict))

empty_set = {1,2,3}
print(empty_set)

cities = {
    "Scotland": "Edinburgh",
    "England": "London",
    "Wales": "Cardiff",
    "Northern Ireland": "Belfast",
}
print(cities)
print(cities["Scotland"])

if "Wales" in cities:
    print("Yes")
else:
    print("No")

print(list(cities.keys()))
print(list(cities.values()))
print(list(cities.items()))

for country, city in cities.items():
    print(f"{city} is the capital of {country}.")

print(cities.get("France", "Don't have that one."))

cities["France"] = "Paris"

print(cities.get("France", "Don't have that one."))

cities2 = cities.copy()

cities2["Italy"] = "Rome"

print(cities.get("Italy", "Not in cities"))
print(cities2.get("Italy", "Not in cities2"))

api_response = {
    "results": 10,
    "page": 0,
    "data": [
        {
            "name": "Nigel"
        }
    ]
}

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.intersection(set2))