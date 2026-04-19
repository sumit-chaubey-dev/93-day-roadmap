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

"""

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"The A of {name} has been created with ${balance} in ABCD Bank")
 
    def deposit(self, amount):
        self.balance += amount
        print(f"Your A has {self.balance} USD.")
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("The balance is insufficient.")
        else:
            self.balance -= amount
            print(f"Your A has {self.balance} USD.")
 
    def check(self):
        print(f"The current balance of {self.name} is {self.balance}")
 

# outer loop — A creation
while True:
    Name = input("\nEnter name to open A (or 'exit' to quit): ")
    if Name.lower() == "exit":
        break
    if not Name.replace(" ", "").isalpha():
        print("Enter a correct name.")
        continue
 
    User = Account(Name)
    account_created = True
 
    # inner loop — transaction session
    if account_created:
        while True:
            Choice = input("\nChoose: (d)eposit, (w)ithdraw, (c)heck, or (f)inish: ").lower()
            if Choice == "f":
                break
            elif Choice == "d":
                amt = float(input("Enter deposit amount: "))
                User.deposit(amt)
            elif Choice == "w":
                amt = float(input("Enter withdraw amount: "))
                User.withdraw(amt)
            elif Choice == "c":
                User.check()
            else:
                print("Invalid option.")

"""

"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def greet(self):
        print("HEY! this is User ")

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.permission = ["delete", "ban"]
    def greet(self):
        print(f"Hello Admin {self.name}")

class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.purchase_hist = []
    def greet(self):
     print(f"Welcome {self.name}")

admin_obj = Admin("Sumit", "sumit@college.edu")
customer_obj = Customer("Aryan", "aryan@email.com")

admin_obj.greet()
customer_obj.greet()
print(f"Admin permissions: {admin_obj.permission}")
print(f"Customer history: {customer_obj.purchase_hist}")

"""

"""

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} make a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print(f"{self.name} says Woof")

class cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print(f"{self.name} says Meow") 


class cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print(f"{self.name} says Moo")  


class sheep(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print(f"{self.name} says Baa")


class duck(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print(f"{self.name} says Quack")

d = Dog("Bruno")
c = cat("Whiskers")
b = cow("Bessie")
a = sheep("Dolly")
k = duck("Donald")  


d.speak()
c.speak()
b.speak()
a.speak()
k.speak()

"""

"""
class People:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(People):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def Introduce(self):
        super().Introduce()
        print(f"I am in grade {self.grade}")

class Teacher(People):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def Introduce(self):
        super().Introduce()
        print(f"I teach {self.subject}")


s = Student("Sumit", 18, 12)
t = Teacher("Mr. Sharma", 35, "Mathematics")

s.Introduce()
t.Introduce()

"""