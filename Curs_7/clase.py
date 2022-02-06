class Employee:
    def __init__(self, nume, varsta, sectie, an):
        self.nume = nume
        self.varsta = varsta
        self.sectie = sectie
        self.an = an

    def superAngajat(self):
        if 2022-self.an>10:
            print(self.nume +" e vechi in companie si merita Bonus")
        else:
            print(self.nume +"   nu primeste Bonus")


A695414 = Employee("Vasile", 39, "Marketing", 2010)
A695415 = Employee("Ion", 35, "Marketing",2020)

if A695415.varsta > A695414.varsta:
    print(f'{A695415.nume} are {A695415.varsta} ani')
else:
    print(f'{A695414.nume} are {A695414.varsta} ani')

A695414.superAngajat()
A695415.superAngajat()


class Dog:
    def __init__(self, name, age , rasa):
        sefl.name = 