# number = "10"
# print(type(number))
#
class Person:
    """
    This is a Person class
    It needs name and age ...

    """
    def __init__(self, name, age): # this function will be invoked when a new class is created
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person called {self.name} who is aged {self.age}"

    def birthday(self):
        print(f"Happy birthday, {self.name}! You were {self.age}")
        self.age += 1
        print(f"Now you are {self.age}")

    def is_teenager(self):
        return 12 < self.age < 20

    def calculate_pocket_money(self, weeks):
        rate_of_pocket_money = 10
        print(f"Calculating {self.name}'s pocket money!")
        return weeks * rate_of_pocket_money

    @staticmethod
    def whats_for_dinner(): # does this really belong in this class?
        return "What you're served!"


print(Person.whats_for_dinner())

person = Person("Ethan", 12)
person2 = Person("Emerald", 10)

del person
person.birthday()
person2.birthday()
print(person.is_teenager())
print(person2.is_teenager())
print(person.calculate_pocket_money(4))
print(person2)
print(type(person))

print(person.name)
print(person2.name)

person3 = {"name": "Kevin", "age": 41}
person3 = Person("Kevin", 41)
person3.age

