# =====================================================================
# CODING FOR DATA SCIENCE AND ANALYTICS
# Exercise Session 4: Functions, Scope, and Recursion
# =====================================================================

# ---------------------------------------------------------------------
# EXERCISE 1: Modularization
# ---------------------------------------------------------------------
print("--- EXERCISE 1: MODULARIZATION ---\n")

# Define the function for Fahrenheit conversion
def to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (9/5 * celsius) + 32

# Define the function for Kelvin conversion
def to_kelvin(celsius):
    """Converts Celsius to Kelvin."""
    return celsius + 273.15

user_celsius = float(input("Enter a temperature in Celsius: "))

# Calling the functions and storing the return values
temp_f = to_fahrenheit(user_celsius)
temp_k = to_kelvin(user_celsius)

print(f"{user_celsius}°C is equal to {temp_f:.2f}°F and {temp_k:.2f}K.")
print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 2: Variable Scope and References
# ---------------------------------------------------------------------
print("--- EXERCISE 2: VARIABLE SCOPE AND REFERENCES ---\n")

def modify_data(num, text):
    # Print IDs inside the function BEFORE modification
    print(f"[Inside Function - Before] ID of num:  {id(num)}")
    print(f"[Inside Function - Before] ID of text: {id(text)}")
    
    # Modifying the variables
    num += 1
    text += " updated"
    
    # Print IDs inside the function AFTER modification
    print(f"\n[Inside Function - After] ID of num:  {id(num)} (Notice it changed!)")
    print(f"[Inside Function - After] ID of text: {id(text)} (Notice it changed!)")
    print(f"[Inside Function - After] Values: num={num}, text='{text}'")

# Variables in the main scope
my_number = 10
my_string = "hello"

print(f"[Main - Before call] ID of my_number: {id(my_number)}, Value: {my_number}")
print(f"[Main - Before call] ID of my_string: {id(my_string)}, Value: '{my_string}'\n")

# Call the function
modify_data(my_number, my_string)

print(f"\n[Main - After call] ID of my_number: {id(my_number)}, Value: {my_number}")
print(f"[Main - After call] ID of my_string: {id(my_string)}, Value: '{my_string}'")

# EXPLANATION:
# Both integers and strings are IMMUTABLE objects in Python.
# When we pass them to the function, we pass their reference.
# However, the moment we try to modify them (num += 1 or text += "..."), 
# Python creates entirely NEW objects in memory for the local scope. 
# This is why their IDs change inside the function after modification, 
# while the original variables in the main program remain completely untouched.
print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 3: Recursion: The Factorial
# ---------------------------------------------------------------------
print("--- EXERCISE 3: RECURSION - THE FACTORIAL ---\n")

def factorial(n):
    # Base case: if n is 0, the factorial is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function with 5
result = factorial(5)
print(f"The factorial of 5 is: {result}")  # Expected output: 120
print("\n" + "="*50 + "\n")

# ---------------------------------------------------------------------
# EXERCISE 3: Recursion: The Factorial
# ---------------------------------------------------------------------
print("--- EXERCISE 3: RECURSION - THE FACTORIAL ---\n")

def factorial(n):
    # Base case: if n is 0, the factorial is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function with 5
result = factorial(5)
print(f"The factorial of 5 is: {result}")  # Expected output: 120

# =====================================================================
# HOW RECURSION WORKS IN THIS EXAMPLE (Call Stack Trace):
# =====================================================================
# When factorial(5) is called, it does not immediately compute 120.
# Instead, it pauses and waits for factorial(4) to finish. This creates
# a chain of function calls (the "stack") until it hits the base case.
#
# 1. THE CALLING PHASE (Winding down)
# factorial(5)      # Executes: 5 * factorial(4) 
#   factorial(4)    # Executes: 4 * factorial(3) 
#     factorial(3)  # Executes: 3 * factorial(2) 
#       factorial(2)  # Executes: 2 * factorial(1) 
#         factorial(1)  # Executes: 1 * factorial(0) 
#           factorial(0)  # Base case reached! Returns 1 
#
# 2. THE RETURNING PHASE (Resolving the math)
# Now that factorial(0) is known, Python works its way back up:
#           factorial(0) returns 1
#         factorial(1) evaluates to: 1 * 1 = 1 
#       factorial(2) evaluates to: 2 * 1 = 2 
#     factorial(3) evaluates to: 3 * 2 = 6 
#   factorial(4) evaluates to: 4 * 6 = 24 
# factorial(5) evaluates to: 5 * 24 = 120 
# =====================================================================

print("\n" + "="*50 + "\n")