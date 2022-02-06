#1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.
#Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
#Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate
#the volume of the Parallelepiped

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return (self.length +self.width)*2

    def Area(self):
        return self.length*self.width

    def Display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height


myRectangle = Rectangle(7, 5)
myRectangle.Display()
print(("/*|*\ ")*10)
myParallelepipede = Parallelepipede(7, 5, 2)
print("the volume of myParallelepipede is: ", myParallelepipede.Volume())

print()
print(("\|/ ")*15)
print(("/|\ ")*15)
print()
#2. Define a Book class with the following attributes: Title, Author (Full name), Price.
#Set the View() method to display information for the current book.

class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def View(self):
        print(f'The book  {self.title} written by {self.author} costs {self.price} lei ')
myBook = Book("Ion", "Liviu Rebreanu", 50)
myBook.View()
print()
print(("\|/ ")*15)
print(("/|\ ")*15)
print()

#3. Create a Python class Person with attributes: name and age of type string.
#Create a display() method that displays the name and age of an object created via the Person class.
#Create a child class Student  which inherits from the Person class and which also has a section attribute.
#Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
#Create a student object via an instantiation on the Student class and then test the displayStudent method.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Display(self):
        print(f'The one called {self.name} has {self.age} years old')
class Student(Person):
    def __init__(self,name, age,section ):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        print(f'{self.name} has {self.age} years old and is a student at {self.section}')

S1 = Student("Ion Vasile", "25", "Litere")
S1.displayStudent()


print()
print(("\|/ ")*15)
print(("/|\ ")*15)
print()

# 4.Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

class BankAccount():
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, deposit):
        self.balance = self.balance + deposit

    def Withdrawal(self, withdraw):
        self.balance = self.balance - withdraw

    def bankFees(self):
        self.balance =0.95*self.balance

    def display(self):
        print(f'Account Number :  {self.accountNumber}')
        print(f'Account Name :  {self.name} ')
        print(f'Account Balance : {self.balance} RON ')

newAccount = BankAccount(12345678, "Vasile Ion" , 1000)
newAccount.Withdrawal(300)
newAccount.Deposit(200)
newAccount.bankFees()
newAccount.display()

print()
print(("\|/ ")*15)
print(("/|\ ")*15)
print()

# 5
# 1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 5 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 6 - Create a tableMult() method which creates and displays the multiplication table of a given integer.
# 7. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv.
# 8. Create another listDivPrim() method that gets all the prime divisors of a given integer.
import math

class Computation():
    def __init__(self):
        pass


    # def factorial(self, fact):
    #     fact = 1
    #     self.fact = fact
    #     for i in range(1,n+1):
    #         fact = fact *i
    #     return fact

    def factorial(self, n):
        j = 1
        for i in range(1, n + 1):
            j = j * i
        return j

n=int(input("Input a number to compute the factorial : "))
print(j)