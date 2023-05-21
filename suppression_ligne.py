import pandas as pd

fichier_csv = "C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv"
df = pd.read_csv(fichier_csv)
df_non_vide = df.dropna ()

print(df_non_vide)
print ("lignes vides supprimées")














