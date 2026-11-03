# =====================================================================
# CODING FOR DATA SCIENCE AND ANALYTICS
# Revision Session: Loops, Functions, and Recursion
# =====================================================================

# ---------------------------------------------------------------------
# EXERCISE 1: Sales Accumulator (Sentinel Loop)
# ---------------------------------------------------------------------
print("--- EXERCISE 1: SALES ACCUMULATOR ---\n")

total_sum = 0.0
item_count = 0
is_shopping = True # Sentinel variable

print("Enter item prices. Type 'totale' to finish.")

while is_shopping:
    user_input = input("Enter price: ").lower()
    
    if user_input == "total":
        is_shopping = False
    else:
        # Convert string to float and accumulate
        price = float(user_input)
        total_sum += price
        item_count += 1

print(f"\nReceipt: {item_count} items purchased.")
print(f"Total to pay: ${total_sum:.2f}")
print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 2: Tax Calculator (Default Parameters)
# ---------------------------------------------------------------------
print("--- EXERCISE 2: TAX CALCULATOR ---\n")

# The parameter tax_rate has a default value of 0.20 (20%)
def calculate_net(gross, tax_rate=0.20):
    tax_amount = gross * tax_rate
    net_salary = gross - tax_amount
    return net_salary

my_gross = 2500.0

# 1. Calling the function using the default tax rate
net_default = calculate_net(my_gross)
print(f"Gross: ${my_gross} | Net (Default 20% tax): ${net_default:.2f}")

# 2. Calling the function with a custom tax rate (e.g., 35%)
net_custom = calculate_net(my_gross, 0.35)
print(f"Gross: ${my_gross} | Net (Custom 35% tax): ${net_custom:.2f}")

print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 3: Recursive Fibonacci
# ---------------------------------------------------------------------
print("--- EXERCISE 3: RECURSIVE FIBONACCI ---\n")

def fib_recursive(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

target = 10
result = fib_recursive(target)
print(f"The {target}th Fibonacci number is: {result}")

# DISCUSSION POINT FOR CLASS:
# Recursive Fibonacci is elegant but highly inefficient (O(2^n) time complexity).
# To compute fib(10), it recalculates the same lower values hundreds of times.
# A loop (O(n)) is much faster for this specific mathematical problem.

print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 4: The Collatz Conjecture (Mega-Exercise)
# ---------------------------------------------------------------------
print("--- EXERCISE 4: THE COLLATZ CONJECTURE ---\n")

# 1. The Recursive Function
def collatz(n):
    # Print the current number in the sequence
    print(int(n), end=" ")
    
    # Base case: We reached 1
    if n == 1:
        return 0
        
    # Recursive case: Even number
    elif n % 2 == 0:
        # 1 step + the steps of the next number
        return 1 + collatz(n / 2)
        
    # Recursive case: Odd number
    else:
        return 1 + collatz(3 * n + 1)

# 2. The Main Program (While Loop + Sentinel)
program_running = True

while program_running:
    user_input = input("\nEnter a starting number (or 'esc' to stop): ").lower()
    
    if user_input == "esc":
        print("Closing program...")
        program_running = False
    else:
        starting_number = int(user_input)
        
        print("Sequence: ", end="")
        
        # Call the recursive function and capture the total steps returned
        total_steps = collatz(starting_number)
        
        print(f"\nIt took {total_steps} steps to reach 1.")

print("\n" + "="*50 + "\n")