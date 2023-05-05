
import pandas as pd

def dfGenIndTri(ligneDesTitres, nombreLignesData, sheetName, débutColonneTrimestre, excelPath) : 

    #lecture du fichier excel
    df = pd.read_excel(excelPath, sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)



    #ajouter d'une colonne artificielle "trimestre" dans le dataframe facilitant la création du graphe associé
    valeurNouvelleColonne = []
    for i in range(débutColonneTrimestre,débutColonneTrimestre + 4) :
        valeurNouvelleColonne.append(df.columns[i])
    df["trimestre"] = valeurNouvelleColonne


    #ajout de nouvelles colonnes dans le dataframe pour chaque valeur de l'indicateur, en fonction du trimestre
    ligne = 0
    for indicateur in df.Indicateur :
        valeurPourIndicateur = []
        for i in range(0, nombreLignesData) :
            valeurPourIndicateur.append(df.iloc[ligne][df["trimestre"]][i])
        df[indicateur] = valeurPourIndicateur
        ligne += 1



    return df


def concatenate(list_of_list):
    list=[]
    for i in range(len(list_of_list)):
        list+=list_of_list[i]
    return list
