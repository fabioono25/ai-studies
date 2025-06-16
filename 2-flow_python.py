# conditions
num = 10
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# loops
for i in range(5):
    print("Loop iteration:", i)

list_names = ["Alice", "Bob", "Charlie"]
for name in list_names:
    print("Hello,", name)

# while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# functions
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

print(greet("Alice"))

# num = input("Enter a number: ")
# try:
#     num = int(num)
#     print("You entered the number:", num)
# except ValueError:
#     print("That's not a valid number!")

# find a prime number
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # explanation: check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True
  
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
    
def add(a, b):
    """Function to add two numbers."""
    return a + b
  
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}.")
        break
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        
# factorial function
def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result