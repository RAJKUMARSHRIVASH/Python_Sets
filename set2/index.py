### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#  Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break  # Stop the loop if number is greater than 500

    if number > 150:
        continue  # Skip the number if it's greater than 150

    if number % 5 == 0:
        print(number)

### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Example usage
s1 = "Hello, world!"
s2 = "Python"
s3 = append_in_middle(s1, s2)
print(s3)


### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

def arrange_characters(string):
    lowercase = ""
    uppercase = ""

    for char in string:
        if char.islower():
            lowercase += char
        else:
            uppercase += char

    arranged_string = lowercase + uppercase
    return arranged_string

# Example usage
given_string = "aBcDeFgHiJkLmN"
arranged_string = arrange_characters(given_string)
print(arranged_string)


### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:
def concatenate_lists(list1, list2):
    new_list = [a + b for a, b in zip(list1, list2)]
    return new_list

# Example usage
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = concatenate_lists(list1, list2)
print(result)

# Problem 6: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate_lists(list1, list2):
    new_list = [a + b for a in list1 for b in list2]
    return new_list

# Example usage
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = concatenate_lists(list1, list2)
print(result)

### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# **Given**
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

def iterate_lists(list1, list2):
    length = min(len(list1), len(list2))

    for i in range(length):
        print(list1[i], list2[len(list2) - i - 1])

# Example usage
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
iterate_lists(list1, list2)

### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dict = {employee: defaults for employee in employees}

print(employee_dict)

### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

{'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)

### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

nested_tuple = ((11, [22, 33]), (44, 55), (66, 77))

modified_tuple = tuple((item[0], [222] + item[1][1:]) if isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], list) else item for item in nested_tuple)

print(modified_tuple)

