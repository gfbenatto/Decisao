#!/usr/bin/python

num1 = input("Digite o primeiro numero. ")
num2 = input("Digite o segundo numero. ")
num3 = input("Digite o terceiro numero. ")

if num1 > num2 and num1 > num3 and num2 > num3:
    print("O maior numero e o:",num1,"e o menor numero e o: ",num3)
elif num2 > num1 and num2 > num3 and num1 > num3:
    print("O maior numero e o:",num2,"e o menor numero e o: ",num3)
elif num3 > num1 and num3 > num2 and num1 > num2:
    print("O maior numero e o:",num3,"e o menor numero e o: ",num2)
elif num1 > num2 and num1 > num3 and num3 > num2:
    print("O maior numero e o:",num1,"e o menor numero e o: ",num2)
elif num2 > num1 and num2 > num3 and num3 > num1:
    print("O maior numero e o:",num2,"e o menor numero e o: ",num1)
elif num3 > num1 and num3 > num2 and num2 > num1:
    print("O maior numero e o:",num3,"e o menor numero e o: ",num1)
else:
    print("Ha numeros iguais.")
