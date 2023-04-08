import os



#Chemin absolu du répertoire de travail (chemin vers app_many_pages)
root_directory = os.path.abspath(os.path.dirname(__file__))

rep_parent = os.path.dirname(root_directory)    #(projet cassiopé)

chemin_absolu_rep_parent = os.path.abspath(rep_parent)



#Chemin absolu des fichiers excels
excel_path = os.path.join(chemin_absolu_rep_parent, 'assets\\Saisie-2023-INDICATEUR-DE-SUIVI-Ti-2.xlsx')



