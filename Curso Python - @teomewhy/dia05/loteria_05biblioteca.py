import random


def check_input():
    try:
        return int(input("Entre com um numero entre 1 e 15: "))   
            
    except ValueError:
        return "Só é valido com um numero"
    
def check_inverval(numero):
    """checa se o numero passado está entre o intervalo de 1 e 15, considerando ambos
    numero: inteiro"""
    return 1 <= numero <= 15

def valida_entrada():
    """essa função valida a entrada do usuário para garantir a integridade do nosso código"""
    while True:
       numero = check_input()
       if type(numero) != int:
           print(numero)
           continue
       
       if check_inverval(numero):
           return numero


numero_sorte = random.randint(1,15)

for i in range(5):

    numero = valida_entrada()
    
    if numero == numero_sorte:  
        print("Você acertou!")  
        break
    elif numero > numero_sorte: 
        print("Você errou! tente um numero menor")  
    else:   
        print("Você errou! tente um numero maior")  


# %%
