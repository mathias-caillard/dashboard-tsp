import os



#Chemin absolu du répertoire de travail (chemin vers app_many_pages)
root_directory = os.path.abspath(os.path.dirname(__file__))

rep_parent = os.path.dirname(root_directory)    #(projet cassiopé)

chemin_absolu_rep_parent = os.path.abspath(rep_parent)



#Chemin absolu des fichiers excels
excel_path = os.path.join(chemin_absolu_rep_parent, 'assets\\Saisie-2023-INDICATEUR-DE-SUIVI-Ti-2.xlsx')
excel_path2 = os.path.join(chemin_absolu_rep_parent, 'assets\\Historique-Indicateurs-Quadri.xlsx')


#Couleurs pour les graphes
colors_dept=['blue', 'lime', 'yellow', 'grey', 'purple', 'cyan', 'red']
#colors_dept=['navy', 'olive', 'salmon', 'mediumvioletred', 'indigo', 'saddlebrown', 'red']
colors_dir=['green', 'blue', 'purple', 'orange', 'black', 'maroon']


# Définir une palette de couleurs pour chaque trimestre
couleurs_trimestres = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)']


trimestre = ['T1', 'T2', 'T3', 'T4']

def get_colorscale() :
    return 'Tealgrn'


