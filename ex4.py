#!/usr/bin/python

letra = raw_input("Digite uma letra. ")
vogais = ('a','e','i','o','u')


#if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
if letra in vogais: 
    print("Voce digitou uma vogal.")
else:
    print("Voce digitou uma consoante.")
