# ==========================================
# EXERCISE 1 - Swapping Variables
# ==========================================
# We start by assigning the initial values to our variables.
x = 2
y = 5

# To swap them, we cannot just write x = y, because the original value of x (2) 
# would be lost forever. Instead, we use a third "temporary" variable to hold 
# the value of x safely before we overwrite x.
temp = x   # 'temp' now holds 2
x = y      # 'x' now becomes 5 (y's value)
y = temp   # 'y' now becomes 2 (the original x value stored in temp)

print("--- EXERCISE 1 ---")
print("x =", x)
print("y =", y)
print() # Prints an empty line for better readabilit


# ==========================================
# EXERCISE 2 - Temperature Conversion
# ==========================================
# We define our starting temperature in Celsius.
celsius = 25

# We use the mathematical formulas provided to calculate Kelvin and Fahrenheit.
# Python uses the '+' sign for addition, '*' for multiplication, and '/' for division.
# Python follows standard mathematical order of operations.
kelvin = celsius + 273.15
fahrenheit = (9 / 5) * celsius + 32

print("--- EXERCISE 2 ---")
print("Kelvin:", kelvin)
print("Fahrenheit:", fahrenheit)
print()


# ==========================================
# EXERCISE 3 - Time Conversion
# ==========================================
# We have a total amount of seconds that we want to split into hours, minutes, and seconds.
total_seconds = 5920

# 1 hour has 3600 seconds (60 minutes * 60 seconds).
# We use the integer division operator '//' to find out how many full hours fit into 5920.
# Unlike standard division '/', '//' removes the decimal part.
hours = total_seconds // 3600

# We use the modulo operator '%' to find the remainder. 
# This tells us how many seconds are left AFTER extracting the full hours.
remaining_seconds = total_seconds % 3600

# Now we take those remaining seconds and find how many full minutes they contain.
# 1 minute = 60 seconds.
minutes = remaining_seconds // 60

# Finally, the remainder of this last division gives us the leftover seconds.
seconds = remaining_seconds % 60

print("--- EXERCISE 3 ---")
print(hours, "hours :", minutes, "minutes :", seconds, "seconds")
print()


# ==========================================
# EXERCISE 4 - Your First print()
# ==========================================
# A string (text) must be enclosed in quotation marks.
name = "Mario"

print("--- EXERCISE 4 ---")
# To print the contents of a variable, we pass the variable name to print() WITHOUT quotes.
print(name)
print()


# ==========================================
# EXERCISE 5 - Printing a Number
# ==========================================
temperature = 23

print("--- EXERCISE 5 ---")
# Print the initial value
print(temperature)

# We update the variable with a new value. The old value is discarded.
temperature = 28

# The print instruction does NOT change, but the output will change 
# because the variable now holds a different value.
print(temperature)
print()


# ==========================================
# EXERCISE 6 - Print the Cat
# ==========================================
print("--- EXERCISE 6 ---")

# METHOD 1: Using single/double quotes with escape characters (\n)
# The backslash '\' is a special escape character in Python.
# '\n' tells Python to create a New Line.
# '\\' tells Python to print an actual backslash (since a single \ is reserved for escaping).
print(" /\\_/\\\n( o.o )\n > ^ <")
print()

# METHOD 2: Using triple quotes
# Triple quotes (""") allow strings to span across multiple lines 
# without needing the '\n' character manually. 
# We still need to use '\\' to print an actual backslash!
print(""" /\\_/\\
( o.o )
 > ^ <""")
print()


# ==========================================
# EXERCISE 7 - Using F-Strings
# ==========================================
name = "Alice"
age = 21
course = "Data Science"

print("--- EXERCISE 7 ---")
# An f-string starts with the letter 'f' before the quotation marks.
# It allows us to inject variables directly into the string by wrapping them in curly braces {}.
# This is much cleaner than using commas to separate text and variables!
print(f"{name} is {age} years old and studies {course}.")
print()


# ==========================================
# EXERCISE 8 - Temperature Report
# ==========================================
celsius = 25
kelvin = celsius + 273.15
fahrenheit = (9 / 5) * celsius + 32

print("--- EXERCISE 8 ---")
# We use an f-string to combine text and our previously calculated numerical variables.
print(f"{celsius} Celsius = {kelvin} Kelvin = {fahrenheit} Fahrenheit")
