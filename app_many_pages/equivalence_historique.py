from config import *


#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

nom_fichier = "EquivalenceIndicateurs.xlsx"
chemin_fichier = generate_path(nom_fichier)
sheet = "Feuil1"

ligneDesTitres = 1  # Numérotation comme dans les liste, matrices...
nombreLignesData = 19  # Nombre de lignes de données
debutColonneData = 1
finColonneData = 3
df = pd.read_excel(chemin_fichier,sheet_name = sheet, header = ligneDesTitres, nrows = nombreLignesData)


chemin_fichier_historique = generate_path(fichier_historique)
colonnes_titre = 0
debutligne = 3
finligne = 27
df2 = pd.read_excel(chemin_fichier_historique, sheet_name="Global")

equivalence_titre = {}
equivalence_ligne = {}
for i in range(nombreLignesData):
    print(df["Nouveaux indicateurs"][i])
    if isinstance(df["Nouveaux indicateurs"][i], str):
        equivalence_titre[df["Nouveaux indicateurs"][i]] = df["Anciens indicateurs"][i]
        ancien_indic = df["Anciens indicateurs"][i]
        for j in range(debutligne, finligne):
            print(df2.iloc[j, 0])
            if not pd.isna(df2.iloc[j, 0]) and df2.iloc[j, 0] == ancien_indic:
                k=j+2
                equivalence_ligne[df["Nouveaux indicateurs"][i]] = k
                break


def correspondance_equivalence(code_indicateur):
    if code_indicateur in equivalence_ligne:
        return True
    return False


print(equivalence_ligne)
