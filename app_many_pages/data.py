
import pandas as pd
import math
import plotly.graph_objects as go
from app_many_pages import config
from df_data import data_df, titre_df, labels_df
from daf_data import data_daf, titre_daf, labels_daf
from dire_data import data_dire, titre_dire, labels_dire
from drfd_data import data_drfd, titre_drfd, labels_drfd
from drh_data import data_drh, titre_drh, labels_drh
from dri_data import data_dri, titre_dri, labels_dri
from equivalence_historique import equivalence_ligne, equivalence_titre, correspondance_equivalence





#Permet du fusionner les dictionnaires
def fusion_dict(liste_dict):
    new_dict = {}
    for dict in liste_dict:
        new_dict.update(dict)
    return new_dict

def fusion_data(liste_data):      #Input: liste(services) de listes(annees) de dictionnaires (indicateurs)
    new_list = []
    for i in range(len(liste_data[0])):     #Parcours des années
        liste_dict = []
        for j in range(len(liste_data)):        #Parcours des services
            liste_dict.append(liste_data[j][i])
        new_list.append(fusion_dict(liste_dict))
    #Return une liste de dictionnaires ou chaque dictionnaire correspond à une année
    return new_list

donnee = [data_df, data_daf, data_drfd, data_dire, data_drh,data_dri]
new_donnee = fusion_data(donnee)
labels = [labels_df, labels_daf, labels_drfd, labels_dire, labels_drh, labels_dri]
new_labels = fusion_dict(labels)
titre = [titre_df, titre_daf, titre_drfd, titre_dire, titre_drh,titre_dri]
new_titre = fusion_dict(titre)


sheet_names = ["artemis", "CITI", "EPH", "INF", "RS2M", "RST", "Global"]
sheet_i = [1, 2, 3, 4, 5, 6, 0]
annees = config.liste_annee
colonneDebutData = 3
colonneFinData = 34
colonneTitre = 0
df_ligne = [10]     #Calcul bizarre
daf_ligne = [24, 25, 27]
dire_ligne = [19, 20, 26]
drfd_ligne = [17, 18]
drh_ligne = [22, 23]

liste_lignes = df_ligne + daf_ligne + dire_ligne + drfd_ligne + drh_ligne

couleurs = config.colors_dept
departements = config.departements
trimestre = config.trimestre


data_old = [{} for i in range(len(annees))]


#Transformer quadrimestre en trimestre
def quadri_to_tri(tab):
    for i in range(len(tab)):
        #print(tab[i])
        if math.isnan(tab[i]):
            tab[i]=0

    l = []
    l.append(0.75*tab[0])
    l.append(0.25*tab[0] + 0.5*tab[1])
    l.append(0.5*tab[1] + 0.25*tab[2])
    l.append(0.75*tab[2])
    #l.append(sum(l))
    return l



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

def extract_data_numerous(sheet_name, list_line):   #Utile pour l'onglet historique
    tab=[]
    for line in list_line:
        tab_line = extract_data(sheet_name, line)
        tab.append(tab_line)
    return tab

#Data pour l'onglet historique
data_old_df = extract_data_numerous(sheet_names[6], df_ligne)
data_old_daf = extract_data_numerous(sheet_names[6], daf_ligne)
data_old_dire = extract_data_numerous(sheet_names[6], dire_ligne)
data_old_drfd = extract_data_numerous(sheet_names[6], drfd_ligne)
data_old_drh = extract_data_numerous(sheet_names[6], drh_ligne)

def convert_data_annuel(data_old):
    converted_data = []
    for i in range(len(data_old[0])):   #Parcours des années
        tab = []
        for j in range(len(data_old)):   #Parcours des departements
            tab.append(data_old[j][i])
        converted_data.append(tab)
    return converted_data


def extract_data_all_sheet(list_line):  #Utile pour la sélection de l'année
    TAB = []
    for line in list_line:  #Parcours des indicateurs
        tab = []
        for i in range(7):   #Parcours des feuilles
            tab_sheet = extract_data(sheet_names[i], line)
            tab.append(tab_sheet)
        TAB.append(convert_data_annuel(tab))
    return TAB


#Meme chose que extract_data_all_sheet mais pour un seul indicateur
def extract_indic_all_sheet(lineNumber):
    tab = []
    for i in range(7):  # Parcours des feuilles
        tab_sheet = extract_data(sheet_names[i], lineNumber)
        tab.append(tab_sheet)
    return convert_data_annuel(tab)


#Met des 0 si pas de correspondance, met les vrais données sinon
def adapt_old_data(code_indic, liste_old_data):
    TAB = []
    if correspondance_equivalence(code_indic):
        #Cas particulier pour DRH-01 (données tri à mettre en annuelle)
        if code_indic == "DRH-01":
            donnee_correspondante = extract_indic_all_sheet(equivalence_ligne[code_indic])

            # Parcours des années
            for i in range(len(liste_old_data)):
                donnee_correspondante_annuellle = [sum(x) / 3 for x in donnee_correspondante[i]]
                liste_old_data[i][code_indic] = donnee_correspondante_annuellle
        else:
            donnee_correspondante = extract_indic_all_sheet(equivalence_ligne[code_indic])
            #Parcours des années
            for i in range(len(liste_old_data)):
                liste_old_data[i][code_indic] = donnee_correspondante[i]
    else:   #Pas de correspondance
        longueur = len(new_donnee[0][code_indic])
        #Distinction données trimestrielles et annuelles
        if longueur==28 or longueur==30:
            donnee_correspondante = [[0, 0, 0, 0] for j in range(7)]
        else:
            donnee_correspondante = [0 for j in range(longueur)]
        # Parcours des années
        for i in range(len(liste_old_data)):
            liste_old_data[i][code_indic] = donnee_correspondante




def adapt_all_old_data(liste_old_data):
    #Parcours des indicateurs
    for code_indic in new_titre:
        adapt_old_data(code_indic, liste_old_data)


def adapt_new_data(code_indic, liste_new_data):
    longueur = len(liste_new_data[0][code_indic])
    # Distinction données trimestrielles et annuelles (rien à faire si données annuelles)
    if longueur==28:
        for i in range(len(liste_new_data)):
            adapted_data = []
            data_indic = liste_new_data[i][code_indic]
            for j in range(7):
                tab = []
                for k in range(4):
                    tab.append(data_indic[4*j + k])
                adapted_data.append(tab)
            liste_new_data[i][code_indic] = adapted_data
    if longueur==30:
        for i in range(len(liste_new_data)):
            adapted_data = []
            data_indic = liste_new_data[i][code_indic]
            for j in range(6):
                tab = []
                for k in range(4):
                    tab.append(data_indic[5*j + k])
                adapted_data.append(tab)
            adapted_data.append([sum([adapted_data[i][j] for i in range(6)]) for j in range(4)])
            liste_new_data[i][code_indic] = adapted_data


def adapt_all_new_data(liste_new_data):
    for code_indic in liste_new_data[0]:
        adapt_new_data(code_indic, liste_new_data)


def adapt_new_label(dict_label):
    for code_indic, label in dict_label.items():
        longueur = len(label)
        if longueur==28:
            adapted_label = []
            for i in range(7):
                label_dept = []
                for j in range(4):
                    label_dept.append(dict_label[code_indic][4*i + j])
                adapted_label.append(label_dept)
            dict_label[code_indic] = adapted_label
        elif longueur==30:
            adapted_label = []
            for i in range(6):
                label_dept = []
                for j in range(4):
                    label_dept.append(dict_label[code_indic][5 * i + j])
                adapted_label.append(label_dept)
            dict_label[code_indic] = adapted_label

def fusion_old_new_data(new_data):
    old_data = [{} for i in range(len(annees))]
    adapt_all_old_data(old_data)
    adapt_all_new_data(new_data)
    for data_annee in new_data:
        old_data.append(data_annee)
    return old_data

data_complete = fusion_old_new_data(new_donnee)
adapt_new_label(new_labels)
#for data_annee in data_complete:
#    print(data_annee)




#Data pour la sélection d'une année(indicateurs, puis année, puis dept)
data_df = extract_data_all_sheet(df_ligne)
data_daf = extract_data_all_sheet(daf_ligne)
data_dire = extract_data_all_sheet(dire_ligne)
data_drfd = extract_data_all_sheet(drfd_ligne)
data_drh = extract_data_all_sheet(drh_ligne)

#print(data_df)

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

titres_y = extract_titre(liste_lignes)


titres_graphe = [#DF
                 "Total général des indicateurs en heures équivalentes",
                 #DAF
                 "Dépenses de vacataires",
                 "Ressources propres totales",
                 "Total des dépenses hors permanents et vacataires",
                 #DIRE
                 "CA sur contrats de recherche",
                 "Brevets et logiciels déposés",
                 "Contribution au financement de l\'école",
                 #DRFD
                 "Total des publications",
                 "Nombre de doctorants",
                 #DRH
                 "Permanents en ETPT",
                 "Non-permanents en ETPT"
                ]

def extract_effectif():
    # Chemin du fichier excel défini dans config.py
    excel_path = config.excel_path2
    # afficher toutes les colonnes (dans le terminal) des dataframes issues des lectures des fichiers Excel
    pd.set_option('display.max_columns', None)
    ligneNumber = 22    #ligne des effectifs
    TAB = []
    for k in range(7):      #Départements
        df = pd.read_excel(excel_path, sheet_name=sheet_names[k])
        ligne = df.iloc[ligneNumber - 2]  # ligneNumber est la ligne dans le fichier excel
        nouveau_df = ligne.to_frame().T
        tab = []
        for i in range(colonneFinData, colonneDebutData, -4):
            tab_i = []
            for j in range(3):
                tab_i.append(nouveau_df.iloc[0, i - j - 1])
            tab_i = quadri_to_tri(tab_i)
            tab.append(tab_i)
        TAB.append(tab)
    return TAB


effectif_dept = extract_effectif()

def ponderation(data_indic):    #Un seul indicateur en entrée
    TAB=[]
    for i in range(len(data_indic)):   #Années
        tab_i=[]
        for j in range(7):      #Départements
            tab_j=[]
            for k in range(4):      #Trimestres
                if effectif_dept[j][i][k] !=0:
                    tab_j.append(data_indic[i][j][k]/effectif_dept[j][i][k])
                else:
                    tab_j.append(0)
            tab_i.append(tab_j)
        TAB.append(tab_i)
    return TAB

def ponderation_total(data_indic):
    TAB = []
    for i in range(len(data_indic)):  # Années
        tab_i = []
        for j in range(7):  # Départements
            if sum(effectif_dept[j][i]) != 0:
                tab_i.append(sum(data_indic[i][j]) / (sum(effectif_dept[j][i])/4))
            else:
                tab_i.append(0)
        TAB.append(tab_i)
    return TAB

def fig_baton_total(donnees, year, titre_graphe, titre_y):
    fig = go.Figure()
    for i in range(len(donnees)):
        fig.add_trace(go.Bar(x=[departements[i]], y=[donnees[i]],
                             name=departements[i],
                             marker=dict(color=[couleurs[i]])))
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year) + ", pondéré par les effectifs",
                      xaxis_title='Départements',
                      yaxis_title=titre_y)
    return fig


#Même couleur pour un département
def fig_baton_trimestre(donnees, year, titre_graphe, titre_y):
    Y = []
    for i in range(len(donnees)):
        Y.append(
            go.Bar(
                x=[departements[i] + " - " + tri for tri in trimestre],
                y=donnees[i],
                name=departements[i],
                width=0.8,
                marker=dict(color=couleurs[i])
            )
        )

    fig = go.Figure(data=Y)
    fig.update_layout(title=titre_graphe + " en " + str(year) + ", pondéré par les effectifs",
                      xaxis_title='Départements',
                      yaxis_title=titre_y)
    return fig

#Même couleur pour un trimestre (même données que fig_baton_trimestre
def fig_baton_departement(donnees, year, titre_graphe, titre_y):
    Y = []
    for i in range(len(donnees)):
        Y.append(
            go.Bar(
                x=[departements[i] + " - " + tri for tri in trimestre],
                y=donnees[i],
                name=departements[i],
                marker=dict(color=couleurs),
                width=0.8,
            )
        )
    fig = go.Figure(data=Y)
    # Ajout d'un titre
    fig.update_layout(title=titre_graphe + " en " + str(year) + ", pondéré par les effectifs",
                      xaxis_title="Temps",
                      yaxis_title=titre_y)
    return fig

#Utilisée pour la régression polynomiale dans les graphes "comparaison annuelle par trimestre"
def data_moy(data) :
    res = []
    moyT1 = 0
    moyT2 = 0
    moyT3 = 0
    moyT4 = 0
    for d in data :
        moyT1 = moyT1 + d[0]
        moyT2 = moyT2 + d[1]
        moyT3 = moyT3 + d[2]
        moyT4 = moyT4 + d[3]
    res.append(moyT1/len(data))
    res.append(moyT2/len(data))
    res.append(moyT3/len(data))
    res.append(moyT4/len(data))
    return res

dict_titres = {
    'DF-01': "Nombre d\'UP",
    'DF-02': "Nombre d\'étudiants FISE",
    'DF-03': "Nombre d\'étudiants FIPA",
    'DF-04': "Nombre d\'étudiants DNM",
    'DF-05': "Nombre d\'étudiants FTLV",
    'DF-06': "Nombre total d\'étudiants",
    'DRFD-01': "Publications sur Scopus",
    'DRFD-02': "Nombre de doctorants",
    'DRFD-03': "H-index médian",
    'DIRE-01': "Suivi des contrats de recherche",
    'DIRE-02': "Brevets et logiciels déposés",
    'DIRE-03': "Contribution au financement de l\'école",
    'DAF-01': "Dépenses de vacataires",
    'DAF-02': "Ressources propres",
    'DAF-03': "Ressources d\'état",
    'DAF-04': "Total des dépenses hors permanents et vacataires",
    'DAF-05': "Dotation de l\'institut hors permanents et vacataires",
    'DAF-06': "Chiffre d\'affaire annuel de la recherche",
    'DRH-01': "Nombre de permanents en ETPT",
    'DRH-02': "Nombre de non-permanents hors recherche en ETPT",
    'DRH-03': "Nombre de non-permanents recherche en ETPT",
    'DRH-04': "Nombre de post-docs",
    'DRH-05': "Nombre d\'ETP permanent ayant une nationalité étrangère",
    'DRH-06': "Nombre de nationalités étrangères différentes",
    'DRI-01': "Nombre d\'étudiants de TSP partant en stage à l\'étranger",
    'DRI-02': "Nombre d\'étudiants de TSP partant à l\'étranger (académique)",
    'DRI-03': "Nombre d\'étudiants étrangers en échange (stock)",
    'DRI-04': "Nombre  d\'étudiants étrangers, au total, administrativement gérés par TSP – dont DNM comptabilisable par la DF",
    'DRI-05': "Nombre d\'étudiants TSP en double diplôme (entrants et sortants)",
    'DRI-06': "Nombre d\'étudiants étrangers – détail par formation",

}