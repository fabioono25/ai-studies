# integers and floats
age = 25
height = 5.9

# strings
name = "Alice"

# boolean
is_student = True

# list
fruits = ["apple", "banana", "cherry"]

# tuple
coordinates = (10.0, 20.0)

# dictionary
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# set
unique_numbers = {1, 2, 3, 4, 5}

# None
nothing = None

# print the variables

print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)
print("Fruits:", fruits)
print("Coordinates:", coordinates)
print("Person:", person)
print("Unique Numbers:", unique_numbers)
print("Nothing:", nothing)

# check the types of the variables
print("\nVariable Types:")
print("Age type:", type(age))
print("Height type:", type(height))
print("Name type:", type(name))
print("Is Student type:", type(is_student))
print("Fruits type:", type(fruits))
print("Coordinates type:", type(coordinates))
print("Person type:", type(person))
print("Unique Numbers type:", type(unique_numbers))
print("Nothing type:", type(nothing))

# print person's name and age
print("\nPerson's Name:", person["name"])
print("Person's Age:", person["age"])

# append to the list
fruits.append("orange")
print("\nUpdated Fruits List:", fruits)
