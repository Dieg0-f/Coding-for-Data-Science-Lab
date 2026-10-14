# =====================================================================
# CODING FOR DATA SCIENCE AND ANALYTICS
# Exercise Session 2: Booleans, Conditions and Loops - Solutions
# =====================================================================

# ==========================================
# EXERCISE 1: Truth Tables
# ==========================================
print("--- EXERCISE 1: TRUTH TABLES ---")

# --- Approach 1: First approach using repeated blocks (Manual) ---
# --- AND ---
print("--- AND Table ---")
print(f"True and True   -> {True and True}")
print(f"True and False  -> {True and False}")
print(f"False and True  -> {False and True}")
print(f"False and False -> {False and False}")
print()

# --- OR ---
print("--- OR Table ---")
print(f"True or True   -> {True or True}")
print(f"True or False  -> {True or False}")
print(f"False or True  -> {False or True}")
print(f"False or False -> {False or False}")
print()

# --- NOT ---
print("--- NOT Table ---")
print(f"not True  -> {not True}")
print(f"not False -> {not False}")


# --- Approach 2: Automating using range() and arithmetic conditions ---
print("\n[Approach 2: Using range() and arithmetic logic]")
print("A\t\tB\t\tAND\t\tOR")
print("-" * 35)

# The loop runs for i = 0, 1, 2, 3
for i in range(4):
    # i < 2 evaluates to True for 0 and 1, False for 2 and 3
    A = i < 2
    # i % 2 == 0 evaluates to True for 0 and 2 (even), False for 1 and 3 (odd)
    B = i % 2 == 0
    
    # Print variables and their logical operations in a tabular format
    print(f"{A}\t{B}\t{A and B}\t{A or B}")

print("\nA\tNOT")
print("-" * 15)

# The loop runs for i = 0, 1
for i in range(2):
    # i == 0 evaluates to True for 0, False for 1
    A = i == 0
    
    print(f"{A}\t{not A}")

print("\n" + "="*50 + "\n")


# ==========================================
# EXERCISE 2: Grades Conversion
# ==========================================
print("--- EXERCISE 2: GRADES CONVERSION ---")
# We use input() to ask the user, converting the inputs to floats for safety
grade = float(input("Enter the student's numerical grade (0-100): "))
attendance = float(input("Enter the student's attendance percentage (0-100): "))

# 1. Determine the Letter Grade using if/elif/else
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# 2. Determine Pass or Fail
# Both conditions must be met to pass (Grade >= 60 AND Attendance >= 75)
if grade >= 60 and attendance >= 75:
    status = "Pass"
else:
    status = "Fail"
    
# Print the final result
print(f"Result: The student got a '{letter}' and their status is '{status}'.")
print("\n" + "="*50 + "\n")


# ==========================================
# EXERCISE 3: Spelling a Word
# ==========================================
print("--- EXERCISE 3: SPELLING A WORD ---")
word = input("Enter a word to spell: ")

# A for loop naturally iterates through each character of a string
for char in word:
    print(char)

print("\n" + "="*50 + "\n")


# ==========================================
# EXERCISE 4: Fibonacci Sequence
# ==========================================
print("--- EXERCISE 4: FIBONACCI SEQUENCE ---")

# --- Approach 1: Using a FOR loop ---
print("\n[Approach 1: Using a FOR loop]")
f0 = 0
f1 = 1
print("First 20 Fibonacci numbers:")
for i in range(20):
    # Print the current number. (end=" " prevents going to a new line immediately)
    print(f0, end=" ")
    
    # Calculate the next Fibonacci number and update f0 and f1
    fnext = f0 + f1
    f0 = f1
    f1 = fnext
    
print("\n")

# --- Approach 2: Using a WHILE loop ---
print("[Approach 2: Using a WHILE loop]")
f0 = 0
f1 = 1
count = 0  # Counter to keep track of how many numbers we printed

while count < 20:
    print(f0, end=" ")
    
    # Update variables
    fnext = f0 + f1
    f0 = f1
    f1 = fnext
    
    # Increment the counter manually
    count += 1
    
print("\n\n" + "="*50 + "\n")


# ==========================================
# EXERCISE 5: Even or Odd
# ==========================================
print("--- EXERCISE 5: EVEN OR ODD ---")

# --- Part A: Check a single number (No Loop) ---
print("\n[Part A: Single Check]")
# We assume the user enters a valid integer
num = int(input("Enter a number to check if it's even or odd: "))

# The modulo operator (%) returns the remainder of a division. 
# If the remainder of num / 2 is 0, the number is even.
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

# --- Part B: Keep asking until the user types "exit" (While Loop) ---
print("\n[Part B: Continuous Loop until 'exit']")
while True: # Infinite loop, we will break out of it manually
    user_input = input("Enter a number (or type 'exit' to stop): ")
    
    # Check if the user wants to quit
    if user_input == "exit":
        print("Exiting the program. Goodbye!")
        break # This stops the while loop
        
    # Convert input to integer
    num_loop = int(user_input)
    
    if num_loop % 2 == 0:
        print(f"{num_loop} is Even.")
    else:
        print(f"{num_loop} is Odd.")

print("\n" + "="*50 + "\n")


# ==========================================
# EXERCISE 6: Questionnaire Data Quality
# ==========================================
print("--- EXERCISE 6: QUESTIONNAIRE DATA QUALITY ---")

# The given string
answers = "ABAC?BBCA?"

# 1. Initialise the counters before the loop
count_A = 0
count_B = 0
count_C = 0
count_missing = 0

# Iterate through every character in the answers string
for answer in answers:
    if answer == 'A':
        count_A += 1
    elif answer == 'B':
        count_B += 1
    elif answer == 'C':
        count_C += 1
    elif answer == '?':
        count_missing += 1

# 2. Calculate the percentage of missing answers.
# Total answers is the length of the string (which is 10)
total_answers = 10
missing_percentage = (count_missing / total_answers) * 100

# Print the individual counts
print(f"Valid Answers -> A: {count_A}, B: {count_B}, C: {count_C}")
print(f"Missing answers (?): {count_missing}")
print(f"Percentage of missing answers: {missing_percentage}%")

# 3. Print the quality assessment based on the condition
if missing_percentage > 15:
    print("STATUS: Data to review")
else:
    print("STATUS: Acceptable quality")

print("\n" + "="*50 + "\n")