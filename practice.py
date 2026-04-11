# ==============================================================================
# TOPIC: LOGIC AND LOOPS PRACTICE
# ==============================================================================

# --- Subtitle: FizzBuzz Challenge (1-100) ---
"""
n = int(input("Enter the limit for FizzBuzz: "))
for num in range(1, n + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
"""

# --- Subtitle: Number Guessing Game with Hints ---
"""
import random

n = int(input("Enter the maximum range for the game: "))
target = random.randint(1, n)
print(f"I have picked a number between 1 and {n}. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    if guess < target:
        print("Higher")
    elif guess > target:
        print("Lower")
    else:
        print("Congratulations! You guessed the number!")
        break
"""

# ==============================================================================
# TOPIC: FUNCTION PRACTICE
# ==============================================================================

# --- Subtitle: Factorial Calculation using Loops ---
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number to find its factorial: "))
print(f"{num}! = {factorial(num)}")
"""

# --- Subtitle: Password Strength Validator ---
"""
def check_password_strength():
    score = 0
    p = input("Enter your password to check strength: ")
    
    # Check length
    if len(p) >= 8:
        score += 1
    # Check for numbers
    if any(char.isdigit() for char in p):
        score += 1
    # Check for uppercase
    if any(char.isupper() for char in p):
        score += 1
    # Check for special characters
    if any(char in "@#$%&" for char in p):
        score += 1
        
    if score == 4:
        print("Strong password ^=^")
    elif score == 3:
        print("Not Strong ^-^")
    else:
        print("What are you doing brooo, make a strong password -_-")

check_password_strength()
"""