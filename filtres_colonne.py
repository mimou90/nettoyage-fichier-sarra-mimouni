import pandas as pd
df = pd.read_csv("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv")
filtres = ["Credit", "Debit","Service"]
df_trie = df [df["Series_titles_2"].isin(filtres)]
print(df_trie)
