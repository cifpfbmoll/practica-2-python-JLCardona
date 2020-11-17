from os import system
system("cls")
print ("Dame un numero y te diré si es par o impar")
n = int (input("Número: "))
if n % 2 == 0:
    print ("El número ",n," es PAR")
else:
    print ("El número ",n," es IMPAR")