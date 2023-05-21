import pandas as pd
df = pd.read_csv("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv")
df['ID'] = range (1, len(df) + 1)
print (df)

