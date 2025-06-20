# Lists
# Lists are mutable sequences, meaning they can be changed after creation.
# They are defined using square brackets [].

numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry"]

mixed = [1, "apple", 3.14, True]

print(numbers[0])

# negative indexing
print(fruits[-1])  # prints "cherry"

# slicing (start, stop - exclusive, step)
print(mixed[1:3])  # prints ["apple", 3.14].

# modifying lists
numbers.append(6)  # adds 6 to the end of the list
print("After appending 6:", numbers)

numbers.remove(2)  # removes the first occurrence of 2
print("After removing 2:", numbers)

# inserting an element at a specific position
numbers.insert(1, 10)  # inserts 10 at index 1

del numbers[0]  # deletes the first element

fruits.sort()  # sorts the list of fruits in alphabetical order
print("Sorted fruits:", fruits)

fruits.pop()  # removes and returns the last element of the list
print("After popping last fruit:", fruits)

####################################################################################################

# Tuples
# Tuples are immutable sequences, meaning they cannot be changed after creation.
# They are defined using parentheses ().

colors = ("red", "green", "blue")
print("First color:", colors[0])

single_item = ("glass",)  # single item tuple requires a comma
print("Single item tuple:", single_item)

# why using tuples over lists?
# Tuples are generally faster than lists for iteration and can be used as keys in dictionaries.
# They are often used to represent fixed collections of items, such as coordinates or RGB values.

######################################################################################################

# Dictionaries
# Dictionaries are mutable mappings, meaning they can be changed after creation.
# They are defined using curly braces {} with key-value pairs.

student = { "name": "Alice", "age": 20, "grades": [85, 90, 95] }
print("Student name:", student["name"])
print("Student grades:", student["grades"])

student["age"] = 21  # modifying a value
print("Updated student age:", student)
student["major"] = "Computer Science"  # adding a new key-value pair
print("After adding major:", student)

del student["grades"]  # deleting a key-value pair
print("After deleting grades:", student)

#iterate through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

######################################################################################################

# Sets
# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() constructor.

fruits_set = {"apple", "banana", "cherry"}
print("Fruits set:", fruits_set)
fruits_set.add("orange")  # adding an element
print("After adding orange:", fruits_set)

fruits_set.remove("banana")  # removing an element
print("After removing banana:", fruits_set)

# Sets do not allow duplicate elements
fruits_set.add("apple")  # adding a duplicate element has no effect
print("After trying to add duplicate apple:", fruits_set)

test = {1, 1, 2}
print("Set with duplicates removed:", test)  # prints {1, 2}

empty_set = set()  # creating an empty set
print("Empty set:", empty_set)

# union and intersection of sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union of set_a and set_b:", set_a | set_b)  # prints

# intersection
print("Intersection of set_a and set_b:", set_a & set_b)  # prints {3}

# subtraction
print("Set_a minus set_b:", set_a - set_b)  # prints {1, 2}

