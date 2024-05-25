# y = f(x) = x + 10
# ------
# y = f(x) = x * x + 1

# %%
def funcao(x):
    res = x + 10
    return res

# %%

y = funcao(100)
print(y)

# %%

# definição da função

def boraestudar():
    print("boraestudar")

# %%
# invocação da função

boraestudar()

# %%

# primeiro os argumentos obrigatórios, depois os argumentos opicionais: ao colocar b=0 se torna opcional
def soma (a, b=0):
    return a + b

soma(10)
# %%
