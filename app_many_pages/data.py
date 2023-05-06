import os
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as subplt
from app_many_pages import config
from app_many_pages import effectifs



#Transformer quadrimestre en trimestre
def quadri_to_tri(tab):
    l = []
    l.append(0.75*tab[0])
    l.append(0.25*tab[0] + 0.5*tab[1])
    l.append(0.5*tab[1] + 0.25*tab[2])
    l.append(0.75*tab[2])
    #l.append(sum(l))
    return l

sheet_names = ["Global", "artemis", "CITI", "EPH", "INF", "RST", "RS2M"]
annees = [2015, 2016, 2017, 2018, 2019]
colonneDebutData = 3
colonneFinData = 22
colonneTitre = 0
df_ligne = [10]     #Calcul bizarre
daf_ligne = [24, 25, 27]
dire_ligne = [19, 20, 26]
drfd_ligne = [17, 18]
drh_ligne = [22, 23]

liste_lignes = df_ligne + daf_ligne + dire_ligne + drfd_ligne + drh_ligne

def extract_data(sheetName, ligneNumber):
    # Chemin du fichier excel défini dans config.py
    excel_path = config.excel_path2

    # afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
    pd.set_option('display.max_columns', None)


    df = pd.read_excel(excel_path, sheet_name=sheetName)
    ligne = df.iloc[ligneNumber - 2]    #ligneNumber est la ligne dans le fichier excel
    nouveau_df = ligne.to_frame().T
    tab = []
    for i in range(colonneFinData, colonneDebutData, -4):
        tab_i = []
        for j in range(3):
            tab_i.append(nouveau_df.iloc[0, i - j - 1])
        tab_i = quadri_to_tri(tab_i)
        tab.append(tab_i)
    return tab

def extract_data_numerous(sheet_name, list_line):
    tab=[]
    for line in list_line:
        tab_line = extract_data(sheet_name, line)
        tab.append(tab_line)
    return tab

def extract_titre(list_line):
    # Chemin du fichier excel défini dans config.py
    excel_path = config.excel_path2

    # afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
    pd.set_option('display.max_columns', None)

    df = pd.read_excel(excel_path, sheet_name=sheet_names[0])

    titles = []
    for i in list_line:
        titles.append(df.iloc[i-2, 0])
    return titles


