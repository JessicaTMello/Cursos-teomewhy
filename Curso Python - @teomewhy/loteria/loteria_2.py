numero_sorte = 7

for i in range(3):

    while True:
        try:
            numero = int(input("Entre com um numero entre 1 e 15: "))   
            break

        except ValueError:
            print("Só é valido com um numero")

    if numero == numero_sorte:  
        print("Você acertou!")  
        break
    elif numero > numero_sorte: 
        print("Você errou! tente um numero menor")  
    else:   
        print("Você errou! tente um numero maior")  


# %%
