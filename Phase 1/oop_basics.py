# ==============================================================================
# DAY 3 — Object Oriented Programming Basics
# ==============================================================================
# TOPIC: CLASS AND OBJECT
# ==============================================================================

# --- Warm-up 1 — Dog Class ---
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

# --- Warm-up 2 — Rectangle Class with Area Method ---
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

# --- Warm-up 3 — Car Class ---
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
# DAY 4 — Instance Methods and Object State
# ==============================================================================
# TOPIC: INSTANCE METHODS AND LOGIC
# ==============================================================================

# --- Practice 1 — Student Grade Checker with File Saving ---
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

# --- Practice 2 — Bank Account System ---
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

# outer loop — account creation
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


# ==============================================================================
# DAY 5 — Inheritance (Parent / Child Classes)
# ==============================================================================
# TOPIC: INHERITANCE
# ==============================================================================

# --- Practice 1 — User, Admin, Customer ---
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


# ==============================================================================
# DAY 6 — Inheritance Overriding + super()
# ==============================================================================
# TOPIC: METHOD OVERRIDING
# ==============================================================================

# --- Practice 1 — Animal Sound System ---
"""
class Animal:
    def __init__(self, name):
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

# --- Practice 2 — School System (People, Student, Teacher) ---
"""
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(People):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def Introduce(self):
        super().Introduce()
        print(f"I am in grade {self.grade}")

class Teacher(People):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def Introduce(self):
        super().Introduce()
        print(f"I teach {self.subject}")

s = Student("Sumit", 18, 12)
t = Teacher("Mr. Sharma", 35, "Mathematics")

s.Introduce()
t.Introduce()
"""


# ==============================================================================
# DAY 7 — Encapsulation (Private Attributes, Getters, ValueError)
# ==============================================================================
# TOPIC: ENCAPSULATION
# ==============================================================================

# --- Practice 1 — Spaceship Fuel System ---
"""
class Spaceship:
    def __init__(self, fuel):
        self.__fuel = fuel

    def Add_fuel(self):
        a = int(input("enter the amount of fuel u wants to add : "))
        if a < 0:
            raise ValueError("Cannot add negative fuel")
        else:
            self.__fuel += a

    def burn(self, amount):
        if self.__fuel < amount:
            raise ValueError("The fuel is insufficient : ")
        else:
            self.__fuel -= amount

    def check(self):
        print(self.__fuel)

a = Spaceship(2000)
a.check()
a.Add_fuel()
a.check()
a.burn(500)
a.check()
a.burn(99999)
"""

# --- Practice 2 — Election Voting System ---
"""
class Election:
    def __init__(self, name):
        self.name = name
        self.__vote = None
        self.__has_voted = False

    def cast_vote(self, candidate):
        if self.__has_voted == True:
            raise ValueError("The voter alredy have voted ^A^ ")
        else:
            self.__vote = candidate
            self.__has_voted = True
            print(f"{self.name} has voted to {candidate}")

    def get_voted(self):
        raise ValueError("Vote is private")

    def has_voted(self):
        return self.__has_voted

voter1 = Election("Sumit")
voter2 = Election("Raj")

voter1.cast_vote("Candidate A")
voter2.cast_vote("Candidate B")

print(voter1.has_voted())

voter1.get_voted()
"""


# ==============================================================================
# DAY 8 — Polymorphism (Same Method, Different Behavior)
# ==============================================================================
# TOPIC: POLYMORPHISM
# ==============================================================================

# --- Practice 1 — Shape Area System (Small vs Large Classifier) ---
"""
class Area:
    def area(self):
        print("Not implemented")

class Circle(Area):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Area):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.name = "Rectangle"

    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(10, 5), Circle(2), Rectangle(3, 4), Circle(8), Rectangle(2, 2)]
small = []
large = []

for shape in shapes:
    result = shape.area()
    if result > 50:
        large.append(shape)
    else:
        small.append(shape)

print("SMALL:")
for shape in small:
    print(f"{shape.name} - {shape.area()}")

print("LARGE:")
for shape in large:
    print(f"{shape.name} - {shape.area()}")
"""