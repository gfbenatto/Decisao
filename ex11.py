#!/usr/bin/python

salario = input("Digite o salario do colaborador. ")


if salario <= 280.0:
    salarionovo = ((salario * 20) / 100) + salario
    percentu = "20%%"
    aumento = (salario*20)/100 
elif salario > 280.0  and salario < 700.0:
    salarionovo = ((salario * 15) / 100) + salario
    percentu = "15%%"
    aumento = (salario*15)/100
else:
    salarionovo = ((salario * 10) / 100) + salario
    percentu = "10%%"
    aumento = (salario*10)/100

print("O salario antes do reajuste e %7.2f " % salario)
print("A porcentagem de reajuste foi de %s " % percentu)
print("O valor do aumento foi de %7.2f " % aumento)
print("O novo salario e de %7.2f " % salarionovo)
