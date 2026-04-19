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


#A batsman scored runs in 10 overs:
scores = [12, 5, 18, 3, 25, 0, 14, 9, 21, 7]
total_runs = sum(scores)
M = max(scores)
l = len(scores)
m = min(scores)
A = (f"The batsman scored highest {M} in the {scores.index(M) + 1} overs.")
B = (f"The batsman scored lowest {m} in the {scores.index(m) + 1} overs.")
countb = 0
for i in scores:
    if i > 10:
        countb += 1
print(f"Great overs: {countb}")
print(f"Total runs scored: {total_runs}")
print(A)
print(B)
print(sorted(scores))
"""
"""
#Phonebook Manager

phonebook = {
    "Sumit": "123-456-7890",
    "Sara": "987-654-3210",
    "Dvyansh": "555-555-5555",
    "krishna": "111-222-3333",
    "UV": "444-444-4444",
    "Rishabh": "666-777-8888",
}
print(phonebook.get("Sumit", "Not found"))
print(phonebook.get("Raghav", "Not found"))
del phonebook["krishna"]
print(phonebook)

"""

#Live Cricket Tournament Simulator
import random
teams = {
    "india": {
        "players": ["Virat", "Rohit", "Shreyas", "KL Rahul", "Hardik"],"wins": 0, "losses": 0
    },
    "Australia": {
        "players": ["Warner", "Smith", "Starc"], "wins": 0, "losses": 0},
    "England": {
        "players": ["Root", "Stokes", "Archer"], "wins": 0, "losses": 0},
    "Pakistan": {
        "players": ["Babar", "Rizwan", "Shaheen"], "wins": 0, "losses": 0},
}
def simulate_match(team1, team2):
    winner = random.choice([team1, team2])
    if winner == team1:
        teams[team1]["wins"] += 1
        teams[team2]["losses"] += 1
    else:
        teams[team2]["wins"] += 1
        teams[team1]["losses"] += 1
        print(simulate_match())

teams = {
    "India": {"wins": 0, "losses": 0},
    "Australia": {"wins": 0, "losses": 0},
    "England": {"wins": 0, "losses": 0},
    "Pakistan": {"wins": 0, "losses": 0},
}

team_names = list(teams.keys())
print(team_names)