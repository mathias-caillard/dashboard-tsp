import pandas as pd
import math
import copy
from  config import generate_path, fichier_historique_df, fichier_historique_dri, annee_min
import  config as config
from  data.df_data import data_df, titre_df, labels_df
from  data.daf_data import data_daf, titre_daf, labels_daf
from  data.dire_data import data_dire, titre_dire, labels_dire
from  data.drfd_data import data_drfd, titre_drfd, labels_drfd
from  data.drh_data import data_drh, titre_drh, labels_drh
from  data.dri_data import data_dri, titre_dri, labels_dri
from  equivalence_historique import equivalence_ligne, correspondance_equivalence
from  data.data_historique import extract_data, extract_indic_all_sheet, convert_data_annuel, quadri_to_tri


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
titre_y = [titre_df, titre_daf, titre_drfd, titre_dire, titre_drh, titre_dri]
new_titre_y = fusion_dict(titre_y)


annees = config.liste_annee

couleurs = config.colors_dept
departements = config.departements
trimestre = config.trimestre


data_old = [{} for i in range(len(annees))]

#Met des 0 si pas de correspondance, met les vrais données sinon
def adapt_old_data(code_indic, liste_old_data):
    TAB = []
    if correspondance_equivalence(code_indic):
        # Cas particulier pour DF-01, DFRD-01, DRFD-02 (données tri à mettre en annuelle)
        if code_indic in  ["DF-01", "DRFD-01", "DRFD-02"]:
            donnee_correspondante = extract_indic_all_sheet(equivalence_ligne[code_indic])
            # Parcours des années
            for i in range(len(liste_old_data)):
                donnee_correspondante_annuellle = [sum(x)  for x in donnee_correspondante[i]]
                liste_old_data[i][code_indic] = donnee_correspondante_annuellle
        #Cas particulier pour DRH-01 (données tri à mettre en annuelle)
        elif "DRH" in code_indic  and code_indic != "DRH-03":
            donnee_correspondante = extract_indic_all_sheet(equivalence_ligne[code_indic])

            # Parcours des années
            for i in range(len(liste_old_data)):
                #Services DF, DRFD, DIRE, DRI , DCOM
                liste = [0., 0., 0., 0., 0.]
                donnee_correspondante_annuellle = [sum(x) / 3 for x in donnee_correspondante[i]]
                #effectif_ecole = donnee_correspondante_annuellle.pop(-1)
                #liste.insert(0, effectif_ecole)
                liste_old_data[i][code_indic] = liste + donnee_correspondante_annuellle
        else:
            donnee_correspondante = extract_indic_all_sheet(equivalence_ligne[code_indic])
            #Parcours des années
            for i in range(len(liste_old_data)):
                liste_old_data[i][code_indic] = donnee_correspondante[i]
    else:   #Pas de correspondance
        longueur = len(new_donnee[0][code_indic])
        #Distinction données trimestrielles et annuelles
        if longueur==28 or longueur==30:
            donnee_correspondante = [[0., 0., 0., 0.] for j in range(7)]
        elif code_indic=="DAF-06":
            donnee_correspondante = [0. for j in range(longueur + 1)]

        else:
            donnee_correspondante = [0. for j in range(longueur)]
        # Parcours des années
        for i in range(len(liste_old_data)):
            liste_old_data[i][code_indic] = donnee_correspondante

def adapt_all_old_data(liste_old_data):
    #Parcours des indicateurs
    for code_indic in new_titre_y:
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
    elif longueur==30:
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
    elif "DRH" in code_indic  and code_indic != "DRH-03":
        for i in range(len(liste_new_data)):
            adapted_data = []
            data_indic = liste_new_data[i][code_indic]
            for j in range(len(data_indic)):
                adapted_data.append(data_indic[j])
            adapted_data.append(adapted_data.pop(0))
            liste_new_data[i][code_indic] = adapted_data
    elif code_indic=="DAF-06":
        for i in range(len(liste_new_data)):
            adapted_data = []
            data_indic = liste_new_data[i][code_indic]
            for j in range(len(data_indic)):
                adapted_data.append(data_indic[j])
            adapted_data.append(sum(adapted_data))
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
            adapted_label.append(["Ecole T1", "Ecole T2", "Ecole T3", "Ecole T4"])
            dict_label[code_indic] = adapted_label

        elif "DRH" in code_indic and code_indic != "DRH-03" :
            adapted_label=[]
            for i in range(len(dict_label[code_indic])):
                adapted_label.append(dict_label[code_indic][i])
            adapted_label.append(adapted_label.pop(0))
            dict_label[code_indic] = adapted_label
        elif code_indic=="DAF-06":
            adapted_label = []
            for i in range(len(dict_label[code_indic])):
                adapted_label.append(dict_label[code_indic][i])
            adapted_label.append("Ecole Année")
            dict_label[code_indic] = adapted_label

def fusion_old_new_data(new_data):
    old_data = [{} for i in range(len(annees))]
    adapt_all_old_data(old_data)
    adapt_all_new_data(new_data)
    for data_annee in new_data:
        old_data.append(data_annee)
    return old_data

def add_old_data_df(liste_data):
    chemin_fichier = generate_path(fichier_historique_df)
    nombre_lignes = 6
    df = pd.read_excel(chemin_fichier, sheet_name="Feuil1", header=0, nrows=nombre_lignes)
    colonne_debut = 1
    colonne_fin = 5
    for i in range(colonne_debut, colonne_fin + 1):
        annee = int(df.iloc[0, i])
        indice_annee = annee - annee_min
        liste_data[indice_annee]["DF-02"] = 4 *[df.iloc[1, i]]
        liste_data[indice_annee]["DF-03"] = 4 *[df.iloc[2, i]]
        liste_data[indice_annee]["DF-04"] = 4 *[df.iloc[3, i]]
        liste_data[indice_annee]["DF-05"] = 4 *[df.iloc[4, i]]
        liste_data[indice_annee]["DF-06"] = 4 *[df.iloc[5, i]]

def add_old_data_dri(liste_data):
    chemin_fichier = generate_path(fichier_historique_dri)
    nombre_lignes = 18
    df = pd.read_excel(chemin_fichier, sheet_name="Feuil1", nrows=nombre_lignes)
    colonne_debut = 1
    colonne_fin = 6
    for i in range(colonne_debut, colonne_fin + 1):
        annee = int(str(df.columns[i]).split("-")[0])
        indice_annee = annee - annee_min
        if not math.isnan(df.iloc[1, i]):
            liste_data[indice_annee]["DRI-01"] = [df.iloc[1, i]]
        else:
            liste_data[indice_annee]["DRI-01"] = [0.]
        if not math.isnan(df.iloc[2, i]):
            liste_data[indice_annee]["DRI-02"] = [df.iloc[2, i]]
        else:
            liste_data[indice_annee]["DRI-02"] = [0.]
        if not math.isnan(df.iloc[5, i]):
            liste_data[indice_annee]["DRI-03"] = [df.iloc[5, i]]
        else:
            liste_data[indice_annee]["DRI-03"] = [0.]
        if not math.isnan(df.iloc[15, i]):
            liste_data[indice_annee]["DRI-04"] = [df.iloc[15, i]]
        else:
            liste_data[indice_annee]["DRI-04"] = [0.]
        if not math.isnan(df.iloc[3, i]):
            liste_data[indice_annee]["DRI-05"] = [df.iloc[3, i]]
        else:
            liste_data[indice_annee]["DRI-05"] = [0.]
        if not math.isnan(df.iloc[7, i]):
            liste_data[indice_annee]["DRI-06"] = [df.iloc[7, i]]
        else:
            liste_data[indice_annee]["DRI-06"] = [0.]

data_complete = fusion_old_new_data(new_donnee)
adapt_new_label(new_labels)
add_old_data_df(data_complete)
add_old_data_dri(data_complete)

effectifs = [data_complete[i]["DRH-01"][6:12] + [sum(data_complete[i]["DRH-01"][6:12])] for i in range(len(data_complete))]

#Détermine les indicateurs qui nécessite une pondération par les effectifs (où les départements sont comparés)
indic_ponderation = ["DF-01",
                     "DRFD-01", "DRFD-02", "DRFD-03",
                     "DIRE-01", "DIRE-02", "DIRE-03",
                     "DAF-01", "DAF-02", "DAF-03", "DAF-04", "DAF-05", "DAF-06"]

#Pondère les données dont le code est présent dans liste_code_indic
def ponderation_data(liste_data, liste_code_indic, liste_effectif):
    new_liste_data = copy.deepcopy(liste_data)
    # Parcours des indicateurs
    for code_indic in liste_code_indic:
        # Parcours des années
        for i in range(len(liste_data)):
            for j in range(len(liste_data[i][code_indic])):
                if liste_effectif[i][j] != 0:
                    #Si données trimestrielles
                    if isinstance(new_liste_data[i][code_indic][j], list):
                        new_liste_data[i][code_indic][j] = [liste_data[i][code_indic][j][k] / liste_effectif[i][j]  for k in range(len(new_liste_data[i][code_indic][j]))]
                    #Si données annuelles
                    else:
                        new_liste_data[i][code_indic][j] = liste_data[i][code_indic][j] / liste_effectif[i][j]
    return new_liste_data



data_complete_pondere = ponderation_data(data_complete, indic_ponderation, effectifs)



def extract_data_radar():
    data_radar = []
    for i in range(len(config.liste_annee_maj)):
        data_radar_annee = []
        for j in range(len(departements)):
            data_radar_annee_dept = []
            data_radar_annee_dept.append(data_complete_pondere[i]["DF-01"][j] / 100)
            data_radar_annee_dept.append(sum(data_complete_pondere[i]["DIRE-01"][j]) / 10000)
            data_radar_annee_dept.append(data_complete_pondere[i]["DRFD-01"][j])
            data_radar_annee_dept.append(sum(data_complete_pondere[i]["DAF-02"][j]) / 10000)
            data_radar_annee_dept.append(data_complete_pondere[i]["DRFD-02"][j])
            data_radar_annee.append(data_radar_annee_dept)
        data_radar.append(data_radar_annee)
    label_radar = [
        "UP <br>(par 100)",
        "Suivi contrats de recherche<br> (par 10K)",
        "Publications",
        "Ressources propres<br> (par 100K) ",
        "Doctorants"
    ]
    return data_radar, label_radar

data_radar, label_radar = extract_data_radar()


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

#Titres des graphes
dict_titres = {
    'DF-01': "DF-01: Nombre d\'UP",
    'DF-02': "DF-02: Nombre d\'étudiants FISE",
    'DF-03': "DF-03: Nombre d\'étudiants FIPA",
    'DF-04': "DF-04: Nombre d\'étudiants DNM",
    'DF-05': "DF-05: Nombre d\'étudiants FTLV",
    'DF-06': "DF-06: Nombre total d\'étudiants",
    'DRFD-01': "DRFD-01: Publications sur Scopus",
    'DRFD-02': "DRFD-02: Nombre de doctorants",
    'DRFD-03': "DRFD-03: H-index médian",
    'DIRE-01': "DIRE-01: Suivi des contrats de recherche",
    'DIRE-02': "DIRE-02: Brevets et logiciels déposés",
    'DIRE-03': "DIRE-03: Contribution au financement de l\'école",
    'DAF-01': "DAF-01: Dépenses de vacataires",
    'DAF-02': "DAF-02: Ressources propres",
    'DAF-03': "DAF-03: Ressources d\'état",
    'DAF-04': "DAF-04: Total des dépenses hors permanents et vacataires",
    'DAF-05': "DAF-05: Dotation de l\'institut hors permanents et vacataires",
    'DAF-06': "DAF-06: Chiffre d\'affaire annuel de la recherche",
    'DRH-01': "DRH-01: Nombre de permanents en ETPT",
    'DRH-02': "DRH-02: Nombre de non-permanents hors recherche en ETPT",
    'DRH-03': "DRH-03: Nombre de non-permanents recherche en ETPT",
    'DRH-04': "DRH-04: Nombre de post-docs",
    'DRH-05': "DRH-05: Nombre d\'ETP permanent ayant une nationalité étrangère",
    'DRH-06': "DRH-06: Nombre de nationalités étrangères différentes",
    'DRI-01': "DRI-01: Nombre d\'étudiants de TSP partant en stage à l\'étranger",
    'DRI-02': "DRI-02: Nombre d\'étudiants de TSP partant à l\'étranger (académique)",
    'DRI-03': "DRI-03: Nombre d\'étudiants étrangers en échange (stock)",
    'DRI-04': "DRI-04: Nombre  d\'étudiants étrangers, au total, administrativement gérés par TSP – dont DNM comptabilisable par la DF",
    'DRI-05': "DRI-05: Nombre d\'étudiants TSP en double diplôme (entrants et sortants)",
    'DRI-06': "DRI-06: Nombre d\'étudiants étrangers – détail par formation",

}