# %%
idade = int (input("Entre com a sua idade:  "))
cnh = input("Você tem CNH? ")

if idade >= 18 and cnh == "sim" :
    print("Siga em frente")

else:
    print("Preso em nome da lei")

condicao = idade >= 18 and cnh == "sim"
print(condicao)
# %%

print(False * 100)
# %%
