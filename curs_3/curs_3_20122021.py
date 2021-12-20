print("hello Wo")

def adunare():
    print("sum is", 5+6)
adunare()

def adunare_param(a,b):
    print("sum is", a + b)
adunare_param(5, 7)
adunare_param(23, 46)
adunare_param(26, 56.1)

def print_details(nume, varsta, restanta = "0"):
    print(f'Hello {nume}, ai {varsta} ani, te rog plateste {restanta} ron')

print_details("Ionut", "35", "580")
print_details("Vali", "55", )

def isNumberPrim(number):
    return True

print("numarul introdus ", isNumberPrim(10))


def day_of_weseek(today):
    if today == "sambata" or today == "duminica" :
        print("este weekend")
    else:
        print("este doar ", + today)


