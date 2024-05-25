# %%

arquivo = open("arquivo.txt", "a") #o W (é para escrever) e sobescreve o arquivo se for modificado, já o "A" adicicona mais informação sem sobescrever
arquivo.write("./Aysha 2")
arquivo.close() # a cada inclusão de informação nova, precisa abrir, adicionar a inf. e fechar o arquivo

# %%

arquivo = open("arquivo.txt","r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

print(type(conteudo))

# %%

arquivo = open("arquivo.txt","r")
linhas = arquivo.readlines()
arquivo.close()

print(linhas)
# %%

with open("arquivo.txt", "r") as file: #Para abrir, ler e escrever o arquivo é recomendado utilizar o with já que ele vai fechar o arquivo automaticamente
    conteudo = file.read()

print(conteudo)