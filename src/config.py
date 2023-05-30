import os
import pandas as pd

fichier_2023 = "Saisie-2023-INDICATEUR-DE-SUIVI-Ti-2.xlsx"
fichier_2024 = "Saisie-2024-INDICATEUR-DE-SUIVI-Ti-2.xlsx"

liste_fichier = [fichier_2023]

fichier_historique = "Historique-Indicateurs-Quadri.xlsx"
fichier_historique_df = "HistoriqueCTI_BJ.xlsx"
fichier_historique_dri = "HistoriqueDRI.xlsx"

#Chemin absolu du répertoire de travail (chemin vers src)
root_directory = os.path.abspath(os.path.dirname(__file__))

rep_parent = os.path.dirname(root_directory)    #(projet cassiopé)

chemin_absolu_rep_parent = os.path.abspath(rep_parent)


#Chemin absolu des fichiers excels
excel_path = os.path.join(chemin_absolu_rep_parent, 'assets\\' + fichier_2023) #données pour l'année 2023
excel_path2 = os.path.join(chemin_absolu_rep_parent, 'assets\\' + fichier_historique) #historique des données pour les années

def generate_path(nom_fichier):
    return os.path.join(chemin_absolu_rep_parent, 'assets\\' + nom_fichier)

#Récupération des années des historiques
df_annee = dataframe = pd.read_excel(excel_path2, sheet_name = "Global", header=None, nrows=1)
df_annee_cleaned = df_annee.dropna(axis=1).drop(df_annee.columns[0], axis=1)

#Annees pour l'historique
liste_annee = df_annee_cleaned.iloc[0].tolist()
liste_annee.reverse()

#Annees pour la sélection de l'année (le menu déroulant)
liste_annee_selection = liste_annee.copy()
liste_annee_selection.append(2023)
liste_annee_selection.reverse()

annee_min = min(liste_annee_selection)

#Années pour la mise à jour des données
liste_annee_maj = liste_annee_selection.copy()
liste_annee_maj.reverse()



#Couleurs pour les graphes
colors_dept=['blue', 'lime', 'yellow', 'grey', 'purple', 'cyan', 'red']
#colors_dept=['navy', 'olive', 'salmon', 'mediumvioletred', 'indigo', 'saddlebrown', 'red']
colors_dir=['green', 'orange', 'black', 'salmon', 'maroon']

colors_all = colors_dir + colors_dept


# Définir une palette de couleurs pour chaque trimestre
couleurs_trimestres = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)']


trimestre = ['T1', 'T2', 'T3', 'T4']
departements = ["ARTEMIS", "CITI", "EPH", "INF", "RS2M", "RST", "ECOLE"]




