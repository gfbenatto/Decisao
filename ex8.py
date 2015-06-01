#!/usr/bin/python
# -*- coding: utf-8 -*-

#é u prgrama tesao

prod1 = input("Digite o valor do primeiro produto. ")
prod2 = input("Digite o valor do segundo produto. ")
prod3 = input("Digite o valor do terceiro produto. ")

if prod2 > prod1 < prod3:
    print("O primeiro produto e mais barato.")
elif prod1 > prod2 < prod3:
    print("O segundo produto e mais barato.")
elif prod2 > prod3 < prod2:
    print("O terceiro produto e mais barato.")
