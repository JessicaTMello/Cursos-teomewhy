# %%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)

# %%

resposta.status_code
# %%

dados = resposta.json()
# %%

dados[0]["roles"]
# %%

for i in dados:
    print(i["localized_name"])
# %%

df = pd.DataFrame(dados)

df.to_csv("heroes_dota.csv",sep=";")


# %%
