import pandas as pd
df = pd.read_csv("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv")
df = df.drop(columns=['Series_reference','Suppressed','STATUS','UNITS','Subject','Group','Series_title_1','Series_title_3','Series_title_4','Series_title_5'])
df.to_csv ("C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/result.csv", index=False)