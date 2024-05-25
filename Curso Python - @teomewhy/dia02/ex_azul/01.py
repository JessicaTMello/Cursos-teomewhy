# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

escolha = input("Você gostaria de uma garrafa de agua mineral ou com gas? [mineral/gas]")

if escolha == "mineral":
    print("Você me deve R$1,50")

else:
    print("Você me deve R$2,50")