import math
import numpy


#Permet d'ajouter les donnees, titres et labels d'un dataframe (feuille d'un fichier excel comme celui de 2023)
def add_to_dict(df, debut, fin, nombre_ligne, dict_data, dict_titre, dict_label):
    x_axis = df.columns.tolist()[debut: fin + 1]
    for i in range(nombre_ligne):
        data_indic = []
        for j in range(debut, fin + 1):
            #Si la case est un nombre
            if isinstance(df.iloc[i, j], (int, float, numpy.int64 , numpy.float64)) and not math.isnan(df.iloc[i, j]):
                data_indic.append(df.iloc[i, j])
            #Sinon la case n'est pas un nombre
            else:
                data_indic.append(0)
        dict_data[df["REF"][i]] = data_indic
        dict_titre[df["REF"][i]] = df["Indicateur"][i]
        dict_label[df["REF"][i]] = x_axis

