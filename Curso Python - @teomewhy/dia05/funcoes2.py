# %%

def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i

    elif op == "mult":
        total=1
        for i in num:
            total *= i 

    return total

operacao("soma",1,2,3,4,5,6,7,8,9,10)
operacao("mult",1,2,3,4,5,6,7,8,9,10)
# %%

dados = ["jessica", "mello", 29, ["aysha", "yankee", "lessy"]]

nome, sobrenome, *lixo, cachorros = dados

print(nome)
print(sobrenome)
print(cachorros)

# %%

a = 10
b = 20
print(a, b)

a, b = [b, a]

c = a
a = b
b = c
print(a, b)

# %%

x = 10,20
type(x)
# %%
