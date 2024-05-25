# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Entre com uma palavra: ")

quantidade = 0
for i in palavra:
    if i == "a":
        quantidade += 1

print("A letra 'a' possui", quantidade, "ocorrencias na palavra", palavra)