idade = int(input("Entre com a sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
    print("Você não pode beber!")

elif idade > 90:
    print("Cuidade, você já é idoso!")

else:
    print("Você é maior de idade")
    print("Você pode beber a vontade!")


# %%

if 18 <= idade <= 89:
    print("Você é maior de idade")
    print("Você pode beber a vontade!")

elif idade >= 90:
    print("Você precisa se cuidar! Cuidado com a idade")

else:
    print("Você é uma criança, vá para casa!")        