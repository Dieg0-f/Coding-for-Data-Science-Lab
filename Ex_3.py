# =====================================================================
# CODING FOR DATA SCIENCE AND ANALYTICS
# Exercise Session 3
# =====================================================================

import random

# ---------------------------------------------------------------------
# EXERCISE 1: Descriptive Statistics
# ---------------------------------------------------------------------
print("--- EXERCISE 1: DESCRIPTIVE STATISTICS ---\n")

temperatures = [22.5, 24.1, 19.8, 25.3, 21.0, 18.5, 23.2]

# Initialize variables to keep track of the count and the running total.
count = 0
total_sum = 0

# Since we cannot use indexing (like temperatures[0]) to set the initial
# minimum and maximum, we use a boolean "flag" variable.
is_first = True
min_val = 0
max_val = 0

# FIRST PASS: Calculate min, max, count, and sum in a single loop.
for temp in temperatures:
    count += 1
    total_sum += temp
    
    # If this is the very first temperature we are looking at,
    # it must be both the minimum and maximum found so far.
    if is_first:
        min_val = temp
        max_val = temp
        is_first = False # Turn off the flag so this block doesn't run again.
    else:
        # For all subsequent temperatures, compare them against current min and max.
        if temp < min_val:
            min_val = temp
        if temp > max_val:
            max_val = temp

# Calculate interval (range) and the mean (average).
interval = max_val - min_val
mean = total_sum / count

# SECOND PASS: Calculate Variance.
# We must do this in a separate loop because we need the final 'mean' 
# to calculate the squared differences.
sum_squared_diff = 0
for temp in temperatures:
    sum_squared_diff += (temp - mean) ** 2

variance = sum_squared_diff / count

# Print all the calculated statistics formatted to 2 decimal places.
print(f"Temperatures: {temperatures}")
print(f"Minimum:  {min_val}")
print(f"Maximum:  {max_val}")
print(f"Interval: {interval:.2f}")
print(f"Count:    {count}")
print(f"Sum:      {total_sum:.2f}")
print(f"Mean:     {mean:.2f}")
print(f"Variance: {variance:.2f}")
print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 2: Smart Home Automation
# ---------------------------------------------------------------------
print("--- EXERCISE 2: SMART HOME AUTOMATION ---\n")

# This boolean variable acts as a Sentinel. It keeps the loop running
# until a specific condition turns it to False.
system_running = True

print("Welcome to Smart Home OS.")
print("Available inputs: 'sunny', 'cloudy', 'rainy', 'movie'.")

# The loop runs indefinitely as long as system_running is True.
while system_running:
    # Ask the user for input and convert it to lowercase to avoid case-sensitivity issues.
    user_input = input("\nEnter weather or mode (or type 'shutdown' to turn off): ").lower()
    
    # Check the Sentinel condition first.
    if user_input == "shutdown":
        print("Shutting down the Smart Home system. Goodbye!")
        system_running = False # This breaks the loop gracefully.
        
    # IFTTT (If This Then That) Logic Rules for the smart home.
    elif user_input == "sunny":
        print("-> Action: Blinds CLOSED. Light turned COOL WHITE.")
    elif user_input == "cloudy":
        print("-> Action: Blinds OPEN. Light turned WARM.")
    elif user_input == "rainy":
        print("-> Action: Blinds OPEN. Light turned COZY YELLOW.")
    elif user_input == "movie":
        print("-> Action: Weather ignored. Blinds CLOSED. Light turned PURPLE.")
    else:
        # Handle unexpected inputs safely without crashing the program.
        print("-> Error: Unknown input. Please try again.")

print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 3: Stock Market "Random Walk"
# ---------------------------------------------------------------------
print("--- EXERCISE 3: STOCK MARKET RANDOM WALK ---\n")

# Setting a seed ensures the random sequence is the same every time we run the script.
random.seed(123) 

# Initial investment parameters.
price = 100.0
stop_loss = 80.0
take_profit = 130.0

days = 0
# Another Sentinel variable to control the financial simulation loop.
position_open = True 

print("Day    | Price   | Trend")
print("-" * 50)

while position_open:
    days += 1
    
    # Generate a random percentage change between -5% and +5%.
    # randrange(-5, 6) generates an integer from -5 up to 5. We divide by 100 for percentage.
    change_pct = random.randrange(-5, 6) / 100 
    
    # Apply the percentage change to the current price.
    price += price * change_pct
    
    # --- ASCII CHART VISUALIZATION ---
    # To draw the chart, we convert the price into a number of spaces.
    # We subtract 70 so the chart doesn't start too far to the right.
    num_spaces = int(price - 70)
    
    # Prevent negative spaces if the price drops below 70.
    if num_spaces < 0: 
        num_spaces = 0
        
    # Multiply the space character by num_spaces to create the indentation.
    spaces_string = " " * num_spaces
    print(f"Day {days:2} | ${price:6.2f} |{spaces_string}*")
    
    # Check if the price has hit our exit thresholds.
    if price <= stop_loss or price >= take_profit:
        position_open = False # This triggers the end of the simulation.

print("-" * 50)
# Determine if the final trade was a win or a loss.
if price >= take_profit:
    print(f"OUTCOME: Closed in PROFIT at ${price:.2f}")
else:
    print(f"OUTCOME: Closed in LOSS at ${price:.2f}")
    
print(f"Total days position was open: {days}")
print("\n" + "="*50 + "\n")


# ---------------------------------------------------------------------
# EXERCISE 4: The Lucky Game
# ---------------------------------------------------------------------
print("--- EXERCISE 4: THE LUCKY GAME ---\n")

random.seed(42) 

# Define a function to handle the repetitive task of rolling two dice.
def roll_dice():
    # randrange(1, 7) picks a random number from 1 to 6 (7 is exclusive).
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    return d1 + d2

# Phase 1: The First Roll
first_roll = roll_dice()
print(f"First roll: {first_roll}")

# Check immediate win/loss conditions based on the game rules.
if first_roll == 7 or first_roll == 11:
    print("Outcome: YOU WIN!")
elif first_roll == 2 or first_roll == 3 or first_roll == 12:
    print("Outcome: YOU LOSE!")
else:
    # Phase 2: The Continuous Rolling Phase
    # If no immediate win/loss, the first roll becomes the target to match.
    target = first_roll
    print(f"Your target is now: {target}")
    
    # Sentinel variable for the game loop.
    game_over = False
    
    while not game_over:
        new_roll = roll_dice()
        print(f"Rolling... {new_roll}")
        
        # Check for the win/loss conditions of the second phase.
        if new_roll == target:
            print("Outcome: MATCH! YOU WIN!")
            game_over = True # Ends the game.
        elif new_roll == 7:
            print("Outcome: ROLLED A 7! YOU LOSE!")
            game_over = True # Ends the game.

print("\n" + "="*50 + "\n")