#!/usr/bin/python

num1 = input("Digite o primeiro numero. ")
num2 = input("Digite o segundo numero. ")
num3 = input("Digite o terceiro numero. ")

if num2 < num1 > num3:
    print("O maior numero e o: ", num1)
elif num1 < num2 > num3:
    print("O maior numero e o: ",num2)
else:
    print("O maior numero e o: ",num3)
