import pandas as pd
df = pd.read_csv("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv")
filtres = ["Credit", "Debit","Service"]
df_trie = df [df["Series_titles_2"].isin(filtres)]
print(df_trie)
df['ID'] = range (1, len(df) + 1)

print (df_trie)
for index, row in df_trie.iterrows():
    print(row)

df_trie.to_csv("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/result.csv", index=False)
