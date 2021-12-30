# 1.Take two int values from user and print greatest among them

x = int(input("Introdu primul numar: "))
y = int(input("Introdu al doilea numar: "))
if(x>y):
    print(x, " este mai mare decat ", y)
elif(y>x):
    print(y, "este mai mare decat ", x)
else:
    print ("numerele introduse sunt egale")

"""Am incercat sa fac cu .spilt() dar   nu mi-a iesit :(
x,y = int(input("introdu 2 numere: ")).spilt()
"""

"""2.A school has following rules for grading system:

a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A

Ask user to enter marks and print the corresponding grade."""

mark = int(input("Introdu nota:"))
if(mark<25):
    print("nota introdusa reprezinta: F")
elif(mark<45):
    print("nota introdusa reprezinta: E")
elif(mark<50):
    print("nota introdusa reprezinta: D")
elif(mark<60):
    print("nota introdusa reprezinta: C")
elif(mark<80):
    print("nota introdusa reprezinta: B")
else:
    print("nota introdusa reprezinta: A")

#----------------------------------------------------------------


"""3.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity"""

total = float(input("Introdu valoare cumparaturilor: "))
if(total<1001):
    print("valoarea cumapraturilor nu este de peste 1000 si astfel nu poti beneficia de reducere ")
else:
    print("valoarea cumparaturilotr tale este de peste 1000, astfel  vei plati mai putin cu : ",  total*0.1 )

#------------------------------------------------------------------------------------------------------------

"""4.Write an if statement that asks for the user's name via input() function.
If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print "Good morning NAME". (Replace Name with user's name)"""

def user():
    nume = input("Please enter your name: ")
    if nume == "Bond":
        print("Wecome on board 007")
    else:
        print("Good morning {}! ".format(nume))
user()
user()

#--------------------------------------------------------------------------------------------------------------

"""5.Write a Python program to check the validity of password input by users. 

Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""

import re

flag = 0
passwd = input("Enter the password: ")
if not re.search('[0-9]', passwd):
    flag = 1
if not re.search('[a-z]', passwd):
    flag = 1
if not re.search('[A-Z]', passwd):
    flag = 1
if not re.search('[$@#!]', passwd):
    flag = 1
if len(passwd) < 6:
    flag = 1
if (flag == 0):
    print('Password is valid')
else:
    print('Password is invalid')


#--------------------------------------------------------------------------------------------------------------

"""6.Write a Python program that tells a user that the number they entered is not a 5 or a 6"""


def numar():
    number = int(input("introdu numarul: "))
    if number != 5 and number !=6 :
        print("number entered is not a 5 or a 6")
    else:
        print("the number is: ", number)
numar()
numar()
numar()
numar()
numar()



""" 8 We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return true if we are in trouble. """

def hour():
    timp = int(input("introdu ora: "))
    if 0<= timp < 24 and (timp <7 or timp >20):
        print("true")

hour()
hour()
hour()
#-------------------------------------------------------------------------------------------------------

# 7.read three numbers and writes them all in sorted order.

def numbers():
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    c = int(input("Input third number: "))
    if a < b:
        if b < c:
            print(a, "<", b, "<", c)
        else:
            if a < c:
                print(a, "<", c, "<", b)
            else:
                print(c, "<", a, "<", b)
    else:
        if c < b:
            print(c, "<", b, "<", a)
        else:
            if c < a:
                print(b, "<", c, "<", a)
            else:
                print(b, "<", a, "<", c)

numbers()
numbers()

"""
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

"""

#------------------------------------------------------------------------------------------------------

"""9.Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged"""


def text():
    textul = str(input("Intodu un text: "))
    if textul[:3]== "Not":
        print (textul)
    else:
        print("Not", textul)
text()
text()

#-------------------------------------------------------------------------------------------

# 10.Given a string, return true if the string starts with "hi" and false otherwise.


def text():
    textul = str(input("Intodu un text si returneaza true: "))
    if textul[:2]== "hi":
        print("true")
    else:
        print("false")
text()
text()

#_____________________________________________________________________________

# 11.Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def suma():
    a = int(input("Introdu un numar: "))
    b = int(input("Introdu al doilea numar: "))
    sum = a+b
    if 10 < sum < 20:
        print("20")
    else:
        print(sum)
suma()
suma()
suma()
suma()

#-----------------------------------------------------------------------------------------------

"""12.We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11. 
Return true if the given non-negative number is special. """



def nu_special():
    special = int(input("Introdu un numar: "))
    if (special % 11) != "0" or (special % 11) != "1":
        print("true")

  # print(special % 11)
nu_special()
nu_special()


