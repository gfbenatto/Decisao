#!/usr/bin/python

turno = raw_input("Em qual turno voce trabalha? (Digitar M-manutino ou V-Vespertino ou N- Noturno) ")

if turno == 'M':
    print("Bom dia.")
elif turno == 'V':
    print("Boa tarde.")
elif turno == 'N':
    print("Boa noite.")
else:
    print("Valor invalido.")
