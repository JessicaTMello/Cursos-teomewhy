numero = int(input("Entre com um numero entre 1 e 15: "))

numero_sorte = 7

if numero == numero_sorte:
    print("Você acertou!")
elif numero > numero_sorte:
    print("Você errou! tente um numero menor")
else:
    print("Você errou! tente um numero maior")