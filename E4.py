from os import system
system("cls")
print ("Introduce dos números")
a = int (input("Primer número: "))
b = int (input("Segundo número: "))
if a > b:
    print (a," es mayor que ",b)
else:
    print (b," es mayor que ",a)