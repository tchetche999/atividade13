# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
num1 = int(input("insira o primeiro número:"))
num2 = int(input("insira o segundo número"))
num3 = int(input("insira o terceiro número"))

if num1 > num2:
 print(num1)
elif num2 > num1:
 print(num2)
else:
 print(num3)