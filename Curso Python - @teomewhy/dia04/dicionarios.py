# %%

dados = ["jessica", "mello", 29] # %%

nome = dados[0]

# %%

dados = {"nome":"jessica",
         "sobrenome":"mello",
         "idade":29,
         "amigas":["suelem", "joyce","kerolyn"],
         "cachorros": [ {"nome": "aysha", "idade": 2}, {"nome": "Yankee", "idade": 13}]}

nome = dados["nome"]
print(nome)

print(dados["cachorros"][0]["idade"])
# %%

dados.keys()

# %%
dados.values()
# %%
dados.items()
# %%
