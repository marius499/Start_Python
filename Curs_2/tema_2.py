#  Marius Comaneciu tema 2

#tema2

# 1 Display the sum of 5 + 10, using two variables: x and y ***

x = 5
y = 10
print("Suma numerelor 5 si 10 este: ",x+y)


#2 Create 3 variables:
#● One of type int  = 20.
#● One of type float = 10.
#● One of type string = “python"

a = 20
b = 10.0
nume = "python"


# 3 Using function type check the type of :
# ● restanta = 0
# notaFinala = 10.0
# laborator = “Introducere in informatica”


restanta = 0
notaFinala = 10.0
laborator = "Introducere in informatica"
print(type(restanta))
print(type(notaFinala))
print(type(laborator))


# 4. Reads two numbers and multiplies them together and print out their product

primulNumar = int(input("Introdu primul numar: "))
doileaNumar = int(input("Introdu al doilea numar: "))
print ("suma numerelor introduse este: ", primulNumar+doileaNumar)
print ("produsul numerelor este: ", primulNumar*doileaNumar)

# 8 Write a Python program to calculate the length of a string.

calculeaza = "eu merg la mare"
print("lungimea stingului calculeaza este: ", len(calculeaza))


#10. Utilizand tipurile de print pe care vi le-am aratat:
#afisati in consola I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = 1000
quantity = 3
price = 450
format_price = "{:.2f}".format(price)
print("I have ", totalMoney, "dolars so i can buy ",quantity," footbal tickets for ", format_price )


#11. .Build a program to calculate the followings using the input from the user for a, b or r
#• rectangle area and perimeter
#• circle area


lungime = float(input("Introdu lungimea: "))
latime = float(input("Introdu latime: "))
raza = float(input("Introdu raza cercului: "))
PI = 3.1415
print("pentru datele introduse aria este: ", lungime*latime,"iar perimetrul: ",2*(lungime +latime))
print("Aria cercului cu raza: ", raza,"este: ",raza*raza*PI)


