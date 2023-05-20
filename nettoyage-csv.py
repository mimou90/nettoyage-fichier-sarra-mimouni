import csv 
test_csv = "C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv"
lignes_non_vides = []
with open ('test.csv', 'r') as fichier:
    lecteur_csv = csv.reader(fichier)
for ligne in lecteur_csv:
    if '' not in ligne:
        lignes_non_vides.append(ligne)
for ligne in lignes_non_vides :
    print (ligne) 

print("lignes vides supprimées.")




