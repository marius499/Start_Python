numbers = (1,2,3,4,5,6,7,8,9)
pare= 0
impare =0
for i in numbers:
    if i%2==0:
        pare = pare+1
    else:
        impare += 1
print(f'numere pare: ', pare)
print(f'numere impare:', impare)


