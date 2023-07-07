# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"
# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.


def printFunction():
    print("Hello World!")


printFunction()


def Datatypes():
    # integer
    age1 = 25
    age2: int = 30

    print(age1, type(age1))

    # float
    points1 = 20.3
    points2: float = 13.12

    print(points1, type(points1))

    # String
    name = 'Raj'
    name: str = "Raju"

    print(name, type(name))

    # Boolean
    isBooked = True
    isPresent: bool = False

    print(isBooked, type(isBooked))

    # list
    arr = [1, 2, 3, 4, 5, 6]
    numbers: list[int] = [1, 2, 3, 4, 5]

    print(arr, type(arr))

    # tuple
    directions = (45, 60)
    coordinates: tuple[int, int] = (10, 20)

    print(directions, type(directions))

    # dictionary

    person = {"name": 'Raj', "age": 25}
    newPerson: dict[str, any] = {"name": "hello", "age": 12}
    print(person, type(person))

    # set

    alphabets = {"a", "b", 'c'}
    alphabets: set[str] = {'a', 'b', 'c'}

    print(alphabets, type(alphabets))

    print(age1, age2, points1, points2, name, isBooked, isPresent, arr,
          numbers, directions, coordinates, person, newPerson, alphabets)


Datatypes()


# List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

numbers = list(range(1, 11))  # Create a list of numbers from 1 to 10
print("Original list:", numbers)

numbers.append(20)  # Add the number 20 to the list
print("List after adding 20:", numbers)

numbers.remove(3)  # Remove the number 3 from the list
print("List after removing 3:", numbers)

numbers.sort()  # Sort the list in ascending order
print("Sorted list:", numbers)

# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

arr = [10, 20, 30, 40]
sum = sum(arr)
avg = sum / len(arr)

print(f"Sum: {sum}, Average: {avg}")

# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"


def reverseString(string):
    return string[::-1]


inputstr = "Raj"

print(reverseString(inputstr))

# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"


def noOfVowels(string):
    vowels = "AEIOUaeiou"
    count = 0
    for i in string:
        if i in vowels:
            count += 1

    return count


print("no of vowels in this string ", noOfVowels("Rajkumarsen"))

# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
# - *Input*: 13
# - *Output*: "13 is a prime number."

def checkPrime(num):
    if num < 2:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True

print(checkPrime(13))

# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# Example usage
input_number = 5
factorial_result = factorial(input_number)
print(f"Factorial of {input_number} is {factorial_result}.")


# 9.  **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence[:n]  # Return the first n numbers

# Example usage
n = 5
fibonacci_numbers = fibonacci_sequence(n)
print(fibonacci_numbers)

# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

squares = [x**2 for x in range(1, 11)]

print(squares)
