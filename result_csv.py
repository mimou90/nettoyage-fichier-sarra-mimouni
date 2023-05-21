import pandas as pd

fichier_csv = "C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv"
df = pd.read_csv(fichier_csv)
df_non_vide = df.dropna ()

filtres = ["Credit", "Debit","Service"]
df_trie = df [df["Series_title_2"].isin(filtres)]
print(df_trie)

df = df.drop(columns=['Series_reference','Suppressed','STATUS','UNITS','Subject','Group','Series_title_1','Series_title_3','Series_title_4','Series_title_5','Magnitude'])
df.to_csv ("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/result.csv", index=False)

df['ID'] = range (1, len(df) + 1)
print (df)

print (df)

