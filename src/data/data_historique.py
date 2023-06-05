
import src.config
import math
import pandas as pd



sheet_names = ["artemis", "CITI", "EPH", "INF", "RS2M", "RST", "Global"]
colonneDebutData = 3
colonneFinData = 34
annees = src.config.liste_annee



#Transformer quadrimestre en trimestre
def quadri_to_tri(tab):
    for i in range(len(tab)):
        if math.isnan(tab[i]):
            tab[i]=0

    l = []
    l.append(0.75*tab[0])
    l.append(0.25*tab[0] + 0.5*tab[1])
    l.append(0.5*tab[1] + 0.25*tab[2])
    l.append(0.75*tab[2])
    #l.append(sum(l))
    return l

#Input: liste (départements) de listes(données en 2015 et 2022)
#Output: liste (années) de listes (données par départements)
def convert_data_annuel(data_old):
    converted_data = []
    for i in range(len(data_old[0])):   #Parcours des années
        tab = []
        for j in range(len(data_old)):   #Parcours des departements
            tab.append(data_old[j][i])
        converted_data.append(tab)
    return converted_data


def extract_data(sheetName, ligneNumber):
    # Chemin du fichier excel défini dans config.py
    excel_path = src.config.excel_path2

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


def extract_indic_all_sheet(lineNumber):
    tab = []
    for i in range(7):  # Parcours des feuilles
        tab_sheet = extract_data(sheet_names[i], lineNumber)
        tab.append(tab_sheet)
    return convert_data_annuel(tab)






