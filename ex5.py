#!/usr/bin/python

nota1 = input("Digite a primeira nota. ")
nota2 = input("Digite a segunda nota. ")

media = (nota1+nota2)/2

if media == 100:
    print("Aluno aprovado com distincao!")
elif media >= 70:
    print("Aluno Aprovado!")
else:
    print("Aluno reprovado.")
