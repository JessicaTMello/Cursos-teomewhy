# Faça um programa que receba 4 notas, armazene em uma lista e 
# depois mostre a soma dessas notas.

notas = []

for i in range(4):
    n = int(input(f"Entre com a nota {i+1}: "))
    notas.append(n)

soma = sum(notas)

print(soma)