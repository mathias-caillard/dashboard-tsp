from app_many_pages import config
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as subplt


#Chemin du fichier excel défini dans config.py
excel_path = config.excel_path

#afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
pd.set_option('display.max_columns', None)

#Pour construire le plot de df, j'ai essayé d'écrire du code le plus générique possible en utilisant le moins possible de "hardcoded values". Cela permettra de facilier la réutilisation du code
ligneDesTitres = 0  #Numérotation comme dans les liste, matrices...
nombreLignesData = 3    #Nombre de lignes de données
sheetName = '2023-DIRE-Tri'   #Nom de la feuille
débutColonneData = 4    #Première colonne de données
FinColonneData = 33  #Dernière colonne de données
df = pd.read_excel(excel_path,sheet_name = sheetName, header = ligneDesTitres, nrows = nombreLignesData)

#Récupération des titres des colonnes
x_axis = df.columns.tolist()



#définition de l'axe des ordnnées
y_axis = []
for indicateur in df.Indicateur :
    y_axis.append(indicateur)

premiereColonneAnnuelle = 8
indice_annuelle = []
for i in range(6):
    j_annuel = 5*i + premiereColonneAnnuelle
    indice_annuelle.append((j_annuel))


#Regroupement des titres et valeurs voulues pour tracer les figures
labels_annuel, labels_trim = [], []
valeur_annuelle1, valeur_annuelle3 =  [], []
valeur_trim1, valeur_trim3 = [], []

for j in indice_annuelle:
    labels_annuel.append(x_axis[j])
    valeur_annuelle1.append(df.iloc[0,j])
    valeur_annuelle3.append((df.iloc[2,j]))
    valeur_trim1_j, valeur_trim3_j, label_trim_j =[], [], []
    for i in range(4):
        label_trim_j.append(x_axis[j+i-4])
        valeur_trim1_j.append(df.iloc[0,j+i-4])
        valeur_trim3_j.append(df.iloc[2, j + i - 4])
    valeur_trim1.append(valeur_trim1_j)
    valeur_trim3.append(valeur_trim3_j)
    labels_trim.append(label_trim_j)


departement = ['ARTEMIS', 'CITI', 'EPH', 'INF', 'RS2M', 'RST']
trimestre = ['Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4']

def fig_dire_1() : 
    #Création d'une figure avec 6 sous-figure pour y placer des histogrammes
    fig1 = subplt.make_subplots(rows=1, cols=6, shared_yaxes=True, horizontal_spacing=0.05)

    #Ajout des histogrammes dans chacune des sous-figures
    for i in range(6):
        labels_i = labels_trim[i]
        valeur_i = valeur_trim1[i]
        fig1.add_trace(go.Bar(x=labels_i, y=valeur_i, name=labels_i[0][:-3]), row=1, col=i+1)

    # Personnaliser l'apparence du graphique
    fig1.update_layout(title='Suivi des contrats de recherche')

    return fig1



def fig_dire_2():

    #Création d'une figure avec 4 sous-figure pour y placer des histogrammes
    #fig2 = subplt.make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.05)
    fig2 = go.Figure()
    #Ajout des histogrammes dans chacune des sous-figures

    for i in range(4):
        labels_i = []
        valeur_i = []
        for j in range(6):
            labels_i.append(labels_trim[j][i])
            valeur_i.append((valeur_trim1[j][i]))

    for i in range(6):
        fig2.add_trace(go.Bar(x=trimestre, y=valeur_trim1[i], name= departement[i]))

    # Personnaliser l'apparence du graphique
    fig2.update_layout(title='Suivi des contrats de recherche, vision trimestrielle')

    return fig2

def fig_dire_3():
    fig3 = go.Figure()
    labels = []
    valeur= []
    for i in range(4):
        labels_i = []
        valeur_i = []
        for j in range(6):
            labels_i.append(labels_trim[j][i])
            valeur_i.append((valeur_trim1[j][i]))
        labels.append( "ECOLE T" + str(i+1))
        valeur.append(sum(valeur_i))
    fig3.add_trace(go.Scatter(x=labels, y=valeur))

    return fig3



def fig_dire_4():
    fig4 = go.Figure(data=[go.Pie(labels=labels_annuel, values=valeur_annuelle3)])


    # Personnaliser l'apparence du graphique
    fig4.update_layout(title='Contribution au financement de l\'école')
    return fig4
