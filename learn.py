# ==============================================================================
# TOPIC: VARIABLES AND BASIC USER INTERACTION
# ==============================================================================

# --- Subtitle: Greeting and Age Input ---
"""
Name = input("What is your name? ")
Age = int(input("What is your age? "))
print("hello " + Name + ", your age is " + str(Age))
"""

# --- Subtitle: Basic Arithmetic Calculator ---
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
plus = num1 + num2
minus = num1 - num2
times = num1 * num2
divide = num1 / num2
modulus = num1 % num2
print(f"the sum is {plus}")
print(f"The difference is {minus}")
print("the product is ", times)
print("the quotient is ", divide)
print("the modulus is ", modulus)
"""

# ==============================================================================
# TOPIC: CONDITIONAL STATEMENTS
# ==============================================================================

# --- Subtitle: Positive/Negative Number Checker ---
"""
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("It's Zero, LOL hahahaah")
"""

# --- Subtitle: Student Grading System ---
"""
num = int(input("Enter marks (0-100): "))
if num < 0 or num > 100:
    print("Invalid marks!")
if num >= 90:
    print("You got an A grade!")
elif num >= 75 and num < 90:
    print("You got a B grade!")
elif num >= 55 and num < 75:
    print("You got a C grade!")
else:
    print("You failed, better luck next time!")
"""

# ==============================================================================
# TOPIC: LOOPS AND PATTERNS
# ==============================================================================

# --- Subtitle: Finding Factors of a Number ---
"""
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
"""

# --- Subtitle: Half-Pyramid Star Pattern ---
""" 
n = int(input("Enter a number of lines of stars to print: "))
char = "*"
for i in range (1, n + 1):
    print(char * i)
"""

# --- Subtitle: Multiplication Table Generator ---
"""
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(num * i)
"""

# ==============================================================================
# TOPIC: FUNCTIONS AND LOGIC
# ==============================================================================

# --- Subtitle: Greatest Common Divisor (GCD) Function ---
"""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
"""

# --- Subtitle: Armstrong Number Validator ---
"""
def is_Armstrong(n):
    num_len = len(str(n))
    total = 0
    for digit in str(n):
        total += int(digit) ** num_len
    return total == n
num = int(input("Enter a number: "))
if is_Armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number!")
"""

# --- Subtitle: EMI (Loan) Calculator ---
"""
def emi_Cal(P, r, t):
    r = r / (12 * 100)
    formula = (P * r * (1 + r)**t) / ((1 + r)**t - 1)
    return formula
P = int(input("Enter your principal amount: "))
r = int(input("enter the rate: "))
t = int(input("enter the time: "))
result = emi_Cal(P, r, t)
print(result)
"""

# ==============================================================================
# TOPIC: STRING AND DIGIT MANIPULATION
# ==============================================================================

# --- Subtitle: Sum of Digits in a Number ---
"""
num = int(input("enter the number : "))
total = sum(int(digit) for digit in str(num))
print(total)
"""

# --- Subtitle: Product of Digits in a Number ---
"""
num = int(input("enter the number : "))
result = 1
for digit in str(num):
    result *= int(digit)
print(result)
"""

# --- Subtitle: Count Even Digits in a Number ---
"""
num = int(input("Enter the number: "))
count = 0
for digit in str(num):
    if int(digit) % 2 == 0:
        count += 1
print(count)
"""