from config import *


#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

nom_fichier = "EquivalenceIndicateurs.xlsx"
chemin_fichier = generate_path(nom_fichier)
sheet = "Feuil1"

ligneDesTitres = 1  # Numérotation comme dans les liste, matrices...
nombreLignesData = 11  # Nombre de lignes de données
debutColonneData = 1
finColonneData = 3
df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)

equivalence_titre = {}
equivalence_ligne = {}
for i in range(nombreLignesData):
    equivalence_titre[df["Nouveaux indicateurs"][i]] = df["Anciens indicateurs"][i]
    equivalence_ligne[df["Nouveaux indicateurs"][i]] = i



