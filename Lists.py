# Import the random module
import random

# Define an empty list
var = []

# Print the type of var
print(type(var))

# Define var2 with a tuple containing integers and a string
var2 = 152, 254, 366, 675, "098"

# Print var2
print(var2)

# Print the available methods and attributes of var2
print(dir(var2))

# Define numbers as a range object
numbers = range(10)

# Print numbers
print(numbers)

# Print numbers
print(numbers)
# Print the type of numbers
print(type(numbers))

# Convert numbers to a list
numbers = list(numbers)
print(numbers)

# Print the element at index 4 of numbers
print(numbers[4])

# Reverse the order of numbers
numbers.reverse()
print(numbers)

# Print the element at index 4 of numbers
print(numbers[4])

# Print the index of the value 4 in numbers
print(numbers.index(4))

# Access an out-of-range index in numbers
print(numbers[5])

# Reverse the order of numbers
numbers.reverse()
print(numbers)

# Print the length of numbers
print(len(numbers))

# Print the square of each number in numbers
for number in numbers:
    print(number ** 2)

# Print the cube of each number in the range from 0 to 9
for i in range(10):
    print(i ** 3)

# Define a list of lists
list_of_lists = []
list_of_lists.append([0, 1, 2])
list_of_lists.append([0, 1, 2])
list_of_lists.append([0, 1, 2])
list_of_lists.append([0, 1, 2])

# Print list_of_lists
print(list_of_lists)

# Iterate through each element in list_of_lists and print it
for list_element in list_of_lists:
    for element in list_element:
        print(element)

# Define second_list_of_lists using list comprehension
second_list_of_lists = [[0, 1, 2] for i in range(4)]

# Print second_list_of_lists
print(second_list_of_lists)

