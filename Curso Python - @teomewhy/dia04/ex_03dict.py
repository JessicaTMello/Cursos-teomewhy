#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

tipo_sorvete = input("Você gostaria de qual tipo de sorvete? [casquinha/cascão/cestinha] ")

sabor = input("Qual o sabor do sorvete? [morango/creme/chocolate] ")

cobertura = input("Qual a cobertura você deseja? [caramelo/morango/chocolate] ")

valor = 0

sorvetes = {"casquinha": 1.00,
            "cascão": 2.5,
            "cestinha": 4.00}

valor += sorvetes[tipo_sorvete]

coberturas = {"caramelo": 1.50, 
              "morango": 1.50, 
              "chocolate": 1.50,
               "":0}

valor += coberturas[cobertura]

print("Seu sorvete", tipo_sorvete, "de", sabor, "cobertura", cobertura, "custará: R$", valor)