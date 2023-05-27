
from src import config
import pandas as pd
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
import effectifs
import data
from src.data import data_moy
import fonctions
import datetime as dt
from config import *
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

liste_fichier = config.liste_fichier

#Import des couleurs
couleurs = config.colors_dept

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)


trimestre = ['T1', 'T2', 'T3', 'T4']
couleurs_trimestres=config.couleurs_trimestres





ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 4    #Nombre de lignes de données
debutColonneData = 4
finColonneData = 7
sheetName = '2023-DF-Tri'   #Nom de la feuille













df_raw_df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)


df_melt = df_raw_df.melt(id_vars=['REF', 'Indicateur', 'Période', 'Périmètre'],
                       value_vars=['Ecole T1', 'Ecole T2', 'Ecole T3', 'Ecole T4'],
                       var_name='Trimestre', value_name='Nombre')
    
# Create a dictionary with trimesters as keys and start dates as values
trimester_dates = {
        "Ecole T1": pd.to_datetime("2022-01-01"),
        "Ecole T2": pd.to_datetime("2022-04-01"),
        "Ecole T3": pd.to_datetime("2022-07-01"),
        "Ecole T4": pd.to_datetime("2022-10-01"),
    }

# Use map() to add a new "Date" column based on the values in the trimester_dates dictionary
df_melt["Date"] = df_melt["Trimestre"].map(trimester_dates)
df_melt["Date"] = pd.to_datetime(df_melt["Date"])

def get_df_melt_df() :
    return df_melt

def get_df_raw_df() :
    return df_raw_df



def fig_df_1_update(df_arg) :
    fig = px.bar(df_arg, x='Trimestre', y='Nombre', color='Indicateur',
                labels={'Trimestre': 'Trimestres', 'Nombre':'Nombre'},
                #hover_data={"Date": '|%d/%m/%Y'},
                title="Nombre d'étudiants à Télécom Sudparis")

    dates = df_arg['Date'].tolist()
    trimestres = df_arg['Trimestre'].tolist()

    #Suppression doublons
    new_list = [] 
    for i in dates : 
        if i not in new_list: 
            new_list.append(i) 
    dates = new_list

    new_list = [] 
    for i in trimestres : 
        if i not in new_list: 
            new_list.append(i) 
    trimestres = new_list

    new_dates = []
    for date in dates : 
        date = date.strftime('%d/%m/%Y')
        new_dates.append(date)
    
    dates = new_dates
        
    #print(trimestres, flush=True)

    final = []
    for i in range(len(trimestres)) :
        final.append(trimestres[i] + " - " + dates[i])

    fig.update_xaxes(tickvals=[i for i in range(len(final))], ticktext=final)


    return fig

ligneDesTitres = 0  # Numérotation comme dans les liste, matrices...
nombreLignesData = 4  # Nombre de lignes de données
sheetName = '2023-DF-Tri'  # Nom de la feuille
débutColonneTrimestre = 4

df = pd.read_excel(excel_path, sheet_name=sheetName, header=ligneDesTitres, nrows=nombreLignesData)

#ajouter d'une colonne artificielle "trimestre" dans le dataframe facilitant la création du graphe associé
valeurNouvelleColonne = []
for i in range(débutColonneTrimestre,débutColonneTrimestre + 4) :
    valeurNouvelleColonne.append(df.columns[i])
df["trimestre"] = valeurNouvelleColonne


#ajout de nouvelles colonnes dans le dataframe pour chaque type d'étudiant.
ligne = 0
for indicateur in df.Indicateur :
    valeurPourIndicateur = []
    for i in range(0, nombreLignesData) :
        valeurPourIndicateur.append(df.iloc[ligne][df["trimestre"]][i])
    df[indicateur] = valeurPourIndicateur
    ligne += 1


#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)

effectif = effectifs.effectif


def fig_df_1():



    # création de la figure
    fig = px.bar(df, x="trimestre", y=y_axis)
    fig.update_layout(title="Nombre d'étudiants à Télécom Sudparis")

    return fig






#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 1    #Nombre de lignes de données
sheetName = '2023-DF-Annuel'   #Nom de la feuille
débutColonneData = 4
finColonneData = 10
df2 = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#définition de l'axe des abscisses
x_axis_annuel = df2.columns.tolist()[débutColonneData: finColonneData + 1]

#définition de l'axe des ordnnées
y_axis_annuel = []
for indicateur in df2.Indicateur :
    y_axis_annuel.append(indicateur)

valeur_annuel = []
for i in range(débutColonneData, finColonneData + 1):
    valeur_annuel.append(df2.iloc[0, i])

df2['Date'] = pd.to_datetime("2022-01-01")
#print(df2, flush = True)


def get_df_DF_annuel():
    return df2

def fig_df_2_update(df_arg):

    fig = go.Figure()
    if df_arg.empty :
        return fig
    else : 
        effectif = effectifs.effectif

        # Ajouter chaque bâton à la figure
        i = 0
        for col_name in df_arg.columns[débutColonneData: finColonneData + 1]:
            taille = str(int(effectif[i]))
            fig.add_trace(go.Bar(x=[col_name + " (" + taille + ")"], y=[df_arg[col_name].iloc[0]],
                                name=col_name, marker=dict(color = [couleurs[i]])))  # effectif du département entre parenthèse
            i += 1

        # Ajout d'un titre
        fig.update_layout(title="Nombre d\'UP produites par Télécom SudParis", xaxis_title='Départements',
                        yaxis_title=y_axis_annuel[0])

        return fig

def fig_df_2():

    fig = go.Figure()


    effectif = effectifs.effectif

    # Ajouter chaque bâton à la figure
    i = 0
    for col_name in df2.columns[débutColonneData: finColonneData + 1]:
        taille = str(int(effectif[i]))
        fig.add_trace(go.Bar(x=[col_name + " (" + taille + ")"], y=[df2[col_name].iloc[0]/effectif[i]],
                                name=col_name, marker=dict(color = [couleurs[i]])))  # effectif du département entre parenthèse
        i += 1

    # Ajout d'un titre
    fig.update_layout(title="Nombre d\'UP produites par Télécom SudParis, pondéré par les effectifs", xaxis_title='Départements',
                    yaxis_title=y_axis_annuel[0])

    return fig


sheetName = data.sheet_names[6]
line = data.df_ligne[0]
titre = data.extract_titre(data.df_ligne)
annees = data.annees
data_old_1 = data.extract_data(sheetName, line)
data_old = [data_old_1]

def fig_old_df_1():


    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_1[i],
                name=str(annee),
                width=0.8,
            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes de 2015 à 2019, vision annuelle",
                      xaxis_title="Années",
                      yaxis_title=titre[0])


    return fig

def fig_old_tri_df_1():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee) + ' - ' + trimestre[j] for j in range(4)],
                y=data_old_1[i],
                name=str(annee),
                marker=dict(color=couleurs_trimestres),
                width=0.8,
            )
        )
    fig = go.Figure(data=donnee)
    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes de 2015 à 2019, vision trimestrielle",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig

def fig_old_df_1_tot():
    donnee = []
    for i, annee in enumerate(annees):
        donnee.append(
            go.Bar(
                x=[str(annee)],
                y=[sum(data_old_1[i])],
                name=str(annee),
            )
        )

    fig = go.Figure(data=donnee)

    # Ajout d'un titre
    fig.update_layout(title="Total général des indicateurs en heures équivalentes de 2015 à 2019, total annuel",
                      xaxis_title="Années",
                      yaxis_title=titre[0])

    return fig







def fig_old_df_2():
    fig = go.Figure()

    # encoder les trimestre : passer d'un String à une valeur int
    label_encoder = LabelEncoder()
    trimestre_encoded = label_encoder.fit_transform([i + 1 for i, _ in enumerate(trimestre)])

    # Ajouter les traces des années
    for i in range(len(annees)):

        fig.add_trace(go.Scatter(x=trimestre_encoded, y=data_old_1[i], name="Année " + str(annees[i])))
    
    # Générer les données moyennes
    y = data_moy(data_old_1)

    # Courbe pour fitter les points
    degree = 3 
    model = LinearRegression()
    model.fit(np.vander(trimestre_encoded, degree + 1), y)

    # Generation des valeurs préditent
    x_pred = np.arange(min(trimestre_encoded), max(trimestre_encoded), 0.1) 
    y_pred = model.predict(np.vander(x_pred, degree + 1))  

    # Ajouter la régression polynomiale
    fig.add_trace(go.Scatter(x=x_pred, y=y_pred, name="Régression", line=dict(dash='dash', color='black'), marker=dict(size=10), visible='legendonly'))



    fig.update_layout(
        title="Total général des indicateurs en heures équivalentes de " + str(liste_annee[-1]) + " à " + str(liste_annee[0]) + ", comparaison annuelle par trimestre",
        xaxis_title="Années",
        yaxis_title=titre[0],
        xaxis = dict(
            tickvals=[0, 1, 2, 3],
            ticktext=['T1', 'T2', 'T3', 'T4']
        )
    )
    return fig

