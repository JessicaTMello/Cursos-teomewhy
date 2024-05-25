# Faça um programa que receba 4 notas, armazene em uma lista e 
# depois mostre a soma dessas notas.

n1 = int(input("Entre com a nota 1: "))
n2 = int(input("Entre com a nota 2: "))
n3 = int(input("Entre com a nota 3: "))
n4 = int(input("Entre com a nota 4: "))

notas = [n1,n2,n3,n4]

soma = sum(notas)

print(soma)