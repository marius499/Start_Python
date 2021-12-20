def addition():
    a = 10
    b = 45
    print(a + b)


addition()

def addition():
    a = int(input("Enter a number "))
    b = int(input("Please enter another number "))
    print(a + b)


addition()


def user_info(name, age, info):
    '''This  function print name age and city from an argument provided '''

    print("{} is {} years old , from {}".format(name, age, info))

user_info("Ioana", 58, "Brasov" )
#user_info(15, "Bran" )

def application(fname,lname, email, company, *args, **kwargs):
    print("{} {} works ar {}. Her email is {}.".format(fname, lname, company, email))

application("Jess", "Jones", "mail@mail.com", "Alos.org", 75000, hire_date = "September 2010")


# Conditionals

print(1<1)

name = input("What is your name?")
if name == "Marius":
    print("Hello, nice to meet you {}".format(name))
elif name == "Ionut":
    print("Hello, you are a nice person! ")
elif name == "Elena":
    print("Hi, {}, let's have lunch!".format(name))

print("Have a nice day!!")

