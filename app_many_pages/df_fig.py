
from app_many_pages import config
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import effectifs
import datetime as dt

#Import des couleurs
couleurs = config.colors_dept

#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)


ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 4    #Nombre de lignes de données
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

def fig_df_1(df_arg) :
    fig = px.bar(df_arg, x='Trimestre', y='Nombre', color='Indicateur',
                labels={'Trimestre': 'Trimestres', 'Nombre':'Nombre'},
                 hover_data={"Date": '|%d/%m/%Y'},
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
        
    print(trimestres, flush=True)

    final = []
    for i in range(len(trimestres)) :
        final.append(trimestres[i] + " - " + dates[i])

    fig.update_xaxes(tickvals=[i for i in range(len(final))], ticktext=final)


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
for i in range(débutColonneData, finColonneData):
    valeur_annuel.append(df2.iloc[0, i])




def fig_df_2():
    fig = go.Figure()
    effectif = effectifs.effectif

    # Ajouter chaque bâton à la figure
    i = 0
    for col_name in df2.columns[débutColonneData: finColonneData + 1]:
        taille = str(int(effectif[i]))
        fig.add_trace(go.Bar(x=[col_name + " (" + taille + ")"], y=[df2[col_name].iloc[0]],
                             name=col_name, marker=dict(color = [couleurs[i]])))  # effectif du département entre parenthèse
        i += 1

    # Ajout d'un titre
    fig.update_layout(title="Nombre d\'UP produites par Télécom SudParis", xaxis_title='Départements',
                      yaxis_title=y_axis_annuel[0])

    return fig

