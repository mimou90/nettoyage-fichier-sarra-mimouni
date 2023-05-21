import csv
fichier_csv_entree = "C:/Users/sarra/Desktop/dc4 git/nettoyage-fichier-sarra-mimouni/test.csv"
fichier_csv_sortie = "test_sortie.csv"

colonnes_sélectionnees = [ "Period", "Data_value","Series_title_2"]

with open(test_csv, 'r') as fichier_entree, open(fichier_csv_sortie, 'w', newline='') as fichier_sortie:
    lecteur_csv = csv.reader