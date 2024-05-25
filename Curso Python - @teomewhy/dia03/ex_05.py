# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("Entre com o seu nome: ")
nome = nome.lower()

if "mello" in nome or "ferreira" in nome:
    print("Você pertence a familia mello ou ferreira")

else:
    print("Não conheço a sua familia")    
