# ==============================================================================
# DAY 3 — Object Oriented Programming Basics
# ==============================================================================
# TOPIC: CLASS AND OBJECT
# ==============================================================================
 
# --- Subtitle: Warm-up 1 — Dog Class ---
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
 
Dog1 = Dog("Rocky", "Labrador")
Dog2 = Dog("Bella", "Poodle")
Dog3 = Dog("Max", "German Shepherd")
dog4 = Dog("Charlie", "Golden Retriever")
 
for dog in [Dog1, Dog2, Dog3, dog4]:
    print(dog.name, dog.breed)
"""
 
# --- Subtitle: Warm-up 2 — Rectangle Class with Area Method ---
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def area(self):
        return self.width * self.height
 
rect1 = Rectangle(int(input("Enter width: ")), int(input("Enter height: ")))
print("Area of the rectangle is:", rect1.area())
"""
 
# --- Subtitle: Warm-up 3 — Car Class ---
"""
class Car:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
 
car1 = Car("Toyota", 180)
car2 = Car("Honda", 200)
car3 = Car("Ford", 220)
 
for car in [car1, car2, car3]:
    print(car.brand, car.max_speed)
"""
 
 
# ==============================================================================
# TOPIC: INSTANCE METHODS AND LOGIC
# ==============================================================================
 
# --- Subtitle: Practice 1 — Student Grade Checker with File Saving ---
"""
class Grade:
    def __init__(self, student_name, grade):
        self.student_name = student_name
        self.grade = grade
 
    def is_passed(self):
        if self.grade > 40:
            print(f"{self.student_name} has passed with the grade of {self.grade}")
        else:
            print(f"{self.student_name} has failed with the grade of {self.grade}")
 
while True:
    student_name = str(input("Enter student name (or type 'exit' to quit): "))
    if student_name == 'exit':
        break
    elif student_name == '':
        print("Student name cannot be empty. Please try again.")
        continue
    elif not student_name.replace(" ", "").isalpha():
        print("Student name must contain only letters. Please try again.")
        continue
 
    grade = int(input("Enter student grade: "))
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100. Please try again.")
        continue
 
    final = Grade(student_name, grade)
    final.is_passed()
 
    with open("data.txt", "a") as f:
        f.write(f"{student_name}: {grade}\n")
"""
 
 
# ==============================================================================
# TOPIC: OBJECT STATE AND NESTED LOOPS
# ==============================================================================
 
# --- Subtitle: Practice 2 — Bank Account System ---

class account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"The account of {name} has been created with ${balance} in ABCD Bank")
 
    def deposite(self, amount):
        self.balance += amount
        print(f"Your account has {self.balance} USD.")
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("The balance is insufficient.")
        else:
            self.balance -= amount
            print(f"Your account has {self.balance} USD.")
 
    def check(self):
        print(f"The current balance of {self.name} is {self.balance}")
 
# outer loop — account creation
while True:
    Name = input("\nEnter name to open account (or 'exit' to quit): ")
    if Name.lower() == "exit":
        break
    if not Name.replace(" ", "").isalpha():
        print("Enter a correct name.")
        continue
 
    User = account(Name)
    account_created = True
 
    # inner loop — transaction session
    if account_created:
        while True:
            Choice = input("\nChoose: (d)eposit, (w)ithdraw, (c)heck, or (f)inish: ").lower()
            if Choice == "f":
                break
            elif Choice == "d":
                amt = float(input("Enter deposit amount: "))
                User.deposite(amt)
            elif Choice == "w":
                amt = float(input("Enter withdraw amount: "))
                User.withdraw(amt)
            elif Choice == "c":
                User.check()
            else:
                print("Invalid option.")