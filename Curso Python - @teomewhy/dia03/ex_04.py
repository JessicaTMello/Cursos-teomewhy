# Faça um programa que verifique se a pessoa pertence à família “mello”.

nome = input("Entre com seu nome completo: ")

nome = nome.lower()

if "mello" in nome:
    print("Você pertence a familia mello")

else:
    print("Você não pertence a familia mello")
