#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

tipo_sorvete = input("Você gostaria de qual tipo de sorvete? [casquinha/cascão/cestinha] ")

sabor = input("Qual o sabor do sorvete? [morango/creme/chocolate] ")

cobertura = input("Qual a cobertura você deseja? [caramelo/morango/chocolate/sem cobertura] ")

valor = 0

# Essa parte é do tipo de sorvete

if tipo_sorvete == "casquinha":
    valor = valor + 1.00

elif tipo_sorvete == "cascão":
    valor += 2.50

elif tipo_sorvete == "cestinha":
    valor += 4.00

else:
    print("Faça uma escolha valida")

 # Essa parte é da cobertura   

if cobertura == "caramelo":
    valor += 1.50

elif cobertura == "morango":
    valor += 1.50

elif cobertura == "chocolate":
    valor += 1.50

elif cobertura == "sem cobertura":
    valor += 0

elif cobertura == " ": 
    pass   

else:
    print("Faça uma escolha valida")


print("Seu sorvete", tipo_sorvete, "de", sabor, "cobertura", cobertura, "custará: R$", valor)