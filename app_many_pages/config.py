import os
import pandas as pd



#Chemin absolu du répertoire de travail (chemin vers app_many_pages)
root_directory = os.path.abspath(os.path.dirname(__file__))

rep_parent = os.path.dirname(root_directory)    #(projet cassiopé)

chemin_absolu_rep_parent = os.path.abspath(rep_parent)



#Chemin absolu des fichiers excels
excel_path = os.path.join(chemin_absolu_rep_parent, 'assets\\Saisie-2023-INDICATEUR-DE-SUIVI-Ti-2.xlsx') #données pour l'année 2023
excel_path2 = os.path.join(chemin_absolu_rep_parent, 'assets\\Historique-Indicateurs-Quadri-2.xlsx') #historique des données pour les années

#Récupération des années des historiques
df_annee = dataframe = pd.read_excel(excel_path2, sheet_name = "Global", header=None, nrows=1)
df_annee_cleaned = df_annee.dropna(axis=1).drop(df_annee.columns[0], axis=1)

#Annee pour l'historique
liste_annee = df_annee_cleaned.iloc[0].tolist()
liste_annee.reverse()

liste_annee = liste_annee.copy()
#liste_annee.append(2023)
liste_annee.reverse()




#Couleurs pour les graphes
colors_dept=['blue', 'lime', 'yellow', 'grey', 'purple', 'cyan', 'red']
#colors_dept=['navy', 'olive', 'salmon', 'mediumvioletred', 'indigo', 'saddlebrown', 'red']
colors_dir=['green', 'blue', 'purple', 'orange', 'black', 'maroon']


# Définir une palette de couleurs pour chaque trimestre
couleurs_trimestres = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)']


trimestre = ['T1', 'T2', 'T3', 'T4']
departements = ["ARTEMIS", "CITI", "EPH", "INF", "RS2M", "RST", "ECOLE"]

def get_colorscale() :
    return 'Tealgrn'


