from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from   functions.fonction_figure import fig_annuelle_baton, fig_radar, fig_camembert, fig_trim_baton, \
    fig_trim_courbe, fig_dept_trim_baton, fig_radar_all_dept
from   config import colors_dept, colors_all


couleurs = colors_dept
couleurs_all = colors_all


categories_libre = [
    # Fusion avec "categories" de "Choix libre"
    # DF
    {"label": "Global - DF-01: Nombre d\'UP - Total annuel", "value": "df1_tot"},
    {"label": "Global - DF-01: Nombre d\'UP - Graphique en camembert", "value": "df1_cam"},
    {"label": "DF-02: Nombre d\'étudiants FISE", "value": "df2_bat"},
    {"label": "DF-03: Nombre d\'étudiants FIPA", "value": "df3_bat"},
    {"label": "DF-04: Nombre d\'étudiants DNM", "value": "df4_bat"},
    {"label": "DF-05: Nombre d\'étudiants FTLV", "value": "df5_bat"},
    {"label": "DF-06: Nombre total d\'étudiants", "value": "df6_bat"},

    #DRFD
    {"label": "Global - DRFD-01: Publications sur Scopus - Total annuel", "value": "drfd1_tot"},
    {"label": "Global - DRFD-01: Publications sur Scopus - Graphique en camembert", "value": "drfd1_cam"},
    {"label": "Global - DRFD-02: Nombre de doctorants - Total annuel", "value": "drfd2_tot"},
    {"label": "Global - DRFD-02: Nombre de doctorants - Graphique en camembert", "value": "drfd2_cam"},
    {"label": "Global - DRFD-03: H-index médian - Total annuel", "value": "drfd3_tot"},

    #DIRE
    {"label": "Global - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat"},
    {"label": "Global - DIRE-01: Suivi des contrats de recherche - Comparaison entre départements", "value": "dire1_cou"},
    {"label": "Global - DIRE-01: Suivi des contrats de recherche - Total annuel", "value": "dire1_tot"},
    {"label": "Global - DIRE-01: Suivi des contrats de recherche - Graphique en camembert", "value": "dire1_cam"},
    {"label": "Global - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat"},
    {"label": "Global - DIRE-02: Brevets et logiciels déposés - Comparaison entre départements", "value": "dire2_cou"},
    {"label": "Global - DIRE-02: Brevets et logiciels déposés - Total annuel", "value": "dire2_tot"},
    {"label": "Global - DIRE-02: Brevets et logiciels déposés - Graphique en camembert", "value": "dire2_cam"},
    {"label": "Global - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat"},
    {"label": "Global - DIRE-03: Contribution au financement de l\'école - Comparaison entre départements", "value": "dire3_cou"},
    {"label": "Global - DIRE-03: Contribution au financement de l\'école - Total annuel", "value": "dire3_tot"},
    {"label": "Global - DIRE-03: Contribution au financement de l\'école - Graphique en camembert", "value": "dire3_cam"},

    #DAF
    {"label": "Global - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat"},
    {"label": "Global - DAF-01: Dépenses de vacataires - Comparaison entre départements", "value": "daf1_cou"},
    {"label": "Global - DAF-01: Dépenses de vacataires - Total annuel", "value": "daf1_tot"},
    {"label": "Global - DAF-01: Dépenses de vacataires - Graphique en camembert", "value": "daf1_cam"},
    {"label": "Global - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat"},
    {"label": "Global - DAF-02: Ressources propres - Comparaison entre départements", "value": "daf2_cou"},
    {"label": "Global - DAF-02: Ressources propres - Total annuel", "value": "daf2_tot"},
    {"label": "Global - DAF-02: Ressources propres - Graphique en camembert", "value": "daf2_cam"},
    {"label": "Global - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat"},
    {"label": "Global - DAF-03: Ressources d\'état - Comparaison entre départements", "value": "daf3_cou"},
    {"label": "Global - DAF-03: Ressources d\'état - Total annuel", "value": "daf3_tot"},
    {"label": "Global - DAF-03: Ressources d\'état - Graphique en camembert", "value": "daf3_cam"},
    {"label": "Global - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat"},
    {"label": "Global - DAF-04: Total des dépenses hors permanents et vacataires - Comparaison entre départements", "value": "daf4_cou"},
    {"label": "Global - DAF-04: Total des dépenses hors permanents et vacataires - Total annuel", "value": "daf4_tot"},
    {"label": "Global - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en camembert", "value": "daf4_cam"},
    {"label": "Global - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat"},
    {"label": "Global - DAF-05: Dotation de l\'institut hors permanents et vacataires - Comparaison entre départements", "value": "daf5_cou"},
    {"label": "Global - DAF-05: Dotation de l\'institut hors permanents et vacataires - Total annuel", "value": "daf5_tot"},
    {"label": "Global - DAF-06: Chiffre d\'affaire annuel de la recherche - Graphique en bâton", "value": "daf6_bat"},
    {"label": "Global - DAF-06: Chiffre d\'affaire annuel de la recherche - Graphique en camembert", "value": "daf6_cam"},

    #DRH
    {"label": "Global - DRH-01: Nombre de permanents en ETPT - Total annuel", "value": "drh1_tot"},
    {"label": "Global - DRH-01: Nombre de permanents en ETPT - Graphique en camembert", "value": "drh1_cam"},
    {"label": "Global - DRH-02: Nombre de non-permanents hors recherche en ETPT - Total annuel", "value": "drh2_tot"},
    {"label": "Global - DRH-02: Nombre de non-permanents hors recherche en ETPT - Graphique en camembert", "value": "drh2_cam"},
    {"label": "Global - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat"},
    {"label": "Global - DRH-03: Nombre de non-permanents recherche en ETPT - Comparaison entre départements", "value": "drh3_cou"},
    {"label": "Global - DRH-03: Nombre de non-permanents recherche en ETPT - Total annuel", "value": "drh3_tot"},
    {"label": "Global - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en camembert", "value": "drh3_cam"},
    {"label": "Global - DRH-04: Nombre de post-docs - Total annuel", "value": "drh4_tot"},
    {"label": "Global - DRH-04: Nombre de post-docs - Graphique en camembert", "value": "drh4_cam"},
    {"label": "Global - DRH-05: Nombre d\'ETP permanent ayant une nationalité étrangère - Total annuel", "value": "drh5_tot"},
    {"label": "Global - DRH-05: Nombre d\'ETP permanent ayant une nationalité étrangère - Graphique en camembert", "value": "drh5_cam"},
    {"label": "Global - DRH-06: Nombre de nationalités étrangères différentes - Total annuel", "value": "drh6_tot"},
    {"label": "Global - DRH-06: Nombre de nationalités étrangères différentes - Graphique en camembert", "value": "drh6_cam"},

    #DRI
    {"label": "DRI-01: Nombre d\'étudiants de TSP partant en stage à l\'étranger - Graphique en bâton", "value": "dri1_bat"},
    {"label": "DRI-02: Nombre d\'étudiants de TSP partant à l\'étranger (académique) - Graphique en bâton", "value": "dri2_bat"},
    {"label": "DRI-03: Nombre d\'étudiants étrangers en échange (stock) - Graphique en bâton", "value": "dri3_bat"},
    {"label": "DRI-04: Nombre  d\'étudiants étrangers, au total, administrativement gérés par TSP – dont DNM comptabilisable par la DF - Graphique en bâton", "value": "dri4_bat"},
    {"label": "DRI-05: Nombre d\'étudiants TSP en double diplôme (entrants et sortants) - Graphique en bâton", "value": "dri5_bat"},
    {"label": "DRI-06: Nombre d\'étudiants étrangers – détail par formation - Total annuel", "value": "dri6_tot"},

    #ARTEMIS
    {"label": "ARTEMIS - Graphique radar", "value": "radar_artemis"},
    {"label": "ARTEMIS - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_artemis"},
    {"label": "ARTEMIS - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_artemis"},
    {"label": "ARTEMIS - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_artemis"},
    {"label": "ARTEMIS - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_artemis"},
    {"label": "ARTEMIS - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_artemis"},
    {"label": "ARTEMIS - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_artemis"},
    {"label": "ARTEMIS - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_artemis"},
    {"label": "ARTEMIS - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_artemis"},
    {"label": "ARTEMIS - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_artemis"},

    #CITI
    {"label": "CITI - Graphique radar", "value": "radar_citi"},
    {"label": "CITI - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_citi"},
    {"label": "CITI - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_citi"},
    {"label": "CITI - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_citi"},
    {"label": "CITI - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_citi"},
    {"label": "CITI - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_citi"},
    {"label": "CITI - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_citi"},
    {"label": "CITI - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_citi"},
    {"label": "CITI - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_citi"},
    {"label": "CITI - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_citi"},

    #EPH
    {"label": "EPH - Graphique radar", "value": "radar_eph"},
    {"label": "EPH - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_eph"},
    {"label": "EPH - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_eph"},
    {"label": "EPH - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_eph"},
    {"label": "EPH - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_eph"},
    {"label": "EPH - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_eph"},
    {"label": "EPH - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_eph"},
    {"label": "EPH - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_eph"},
    {"label": "EPH - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_eph"},
    {"label": "EPH - DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_eph"},

    #INF
    {"label": "INF - Graphique radar", "value": "radar_inf"},
    {"label": "INF - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_inf"},
    {"label": "INF - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_inf"},
    {"label": "INF - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_inf"},
    {"label": "INF - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_inf"},
    {"label": "INF - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_inf"},
    {"label": "INF - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_inf"},
    {"label": "INF - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_inf"},
    {"label": "INF - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_inf"},
    {"label": "INF- DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_inf"},

    #RS2M
    {"label": "RS2M - Graphique radar", "value": "radar_rs2m"},
    {"label": "RS2M - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_rs2m"},
    {"label": "RS2M - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_rs2m"},
    {"label": "RS2M - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_rs2m"},
    {"label": "RS2M - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_rs2m"},
    {"label": "RS2M - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_rs2m"},
    {"label": "RS2M - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_rs2m"},
    {"label": "RS2M - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_rs2m"},
    {"label": "RS2M - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_rs2m"},
    {"label": "RS2M- DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_rs2m"},

    #RST
    {"label": "RST - Graphique radar", "value": "radar_rst"},
    {"label": "RST - DIRE-01: Suivi des contrats de recherche - Graphique en bâton", "value": "dire1_bat_rst"},
    {"label": "RST - DIRE-02: Brevets et logiciels déposés - Graphique en bâton", "value": "dire2_bat_rst"},
    {"label": "RST - DIRE-03: Contribution au financement de l\'école - Graphique en bâton", "value": "dire3_bat_rst"},
    {"label": "RST - DAF-01: Dépenses de vacataires - Graphique en bâton", "value": "daf1_bat_rst"},
    {"label": "RST - DAF-02: Ressources propres - Graphique en bâton", "value": "daf2_bat_rst"},
    {"label": "RST - DAF-03: Ressources d\'état - Graphique en bâton", "value": "daf3_bat_rst"},
    {"label": "RST - DAF-04: Total des dépenses hors permanents et vacataires - Graphique en bâton", "value": "daf4_bat_rst"},
    {"label": "RST - DAF-05: Dotation de l\'institut hors permanents et vacataires - Graphique en bâton", "value": "daf5_bat_rst"},
    {"label": "RST- DRH-03: Nombre de non-permanents recherche en ETPT - Graphique en bâton", "value": "drh3_bat_rst"},

    #Autres
    {"label": "Global - Graphique radar des départements", "value": "radar_global"},

]


def generate_graphs_libre(selected_annee, value, baseline_graph):


    # Liste des graphiques disponibles
    graphs_libre = {}

    #DF
    if "df1_tot" in value:
        graphs_libre["df1_tot"] = fig_annuelle_baton("DF-01", selected_annee, "Départements", couleurs)
    if "df1_cam" in value:
        graphs_libre["df1_cam"] = fig_camembert("DF-01", selected_annee, couleurs)
    if "df2_bat" in value:
        graphs_libre["df2_bat"] = fig_trim_baton("DF-02", selected_annee, "Temps", None)
    if "df3_bat" in value:
        graphs_libre["df3_bat"] = fig_trim_baton("DF-03", selected_annee, "Temps", None)
    if "df4_bat" in value:
        graphs_libre["df4_bat"] = fig_trim_baton("DF-04", selected_annee, "Temps", None)
    if "df5_bat" in value:
        graphs_libre["df5_bat"] = fig_trim_baton("DF-05", selected_annee, "Temps", None)
    if "df6_bat" in value:
        graphs_libre["df6_bat"] = fig_trim_baton("DF-06", selected_annee, "Temps", None)
    #DRFD
    if "drfd1_tot" in value:
        graphs_libre["drfd1_tot"] = fig_annuelle_baton("DRFD-01", selected_annee, "Départements", couleurs)
    if "drfd1_cam" in value:
        graphs_libre["drfd1_cam"] = fig_camembert("DRFD-01", selected_annee, couleurs)
    if "drfd2_tot" in value:
        graphs_libre["drfd2_tot"] = fig_annuelle_baton("DRFD-02", selected_annee, "Départements", couleurs)
    if "drfd2_cam" in value:
        graphs_libre["drfd2_cam"] = fig_camembert("DRFD-02", selected_annee, couleurs)
    if "drfd3_tot" in value:
        graphs_libre["drfd3_tot"] = fig_annuelle_baton("DRFD-03", selected_annee, "Départements", couleurs)
    #DIRE
    if "dire1_bat" in value:
        graphs_libre["dire1_bat"] = fig_trim_baton("DIRE-01", selected_annee, "Départements", couleurs)
    if "dire1_cou" in value:
        graphs_libre["dire1_cou"] = fig_trim_courbe("DIRE-01", selected_annee, couleurs)
    if "dire1_tot" in value:
        graphs_libre["dire1_tot"] = fig_annuelle_baton("DIRE-01", selected_annee, "Départements", couleurs)
    if "dire1_cam" in value:
        graphs_libre["dire1_cam"] = fig_camembert("DIRE-01", selected_annee, couleurs)
    if "dire2_bat" in value:
        graphs_libre["dire2_bat"] = fig_trim_baton("DIRE-02", selected_annee, "Départements", couleurs)
    if "dire2_cou" in value:
        graphs_libre["dire2_cou"] = fig_trim_courbe("DIRE-02", selected_annee, couleurs)
    if "dire2_tot" in value:
        graphs_libre["dire2_tot"] = fig_annuelle_baton("DIRE-02", selected_annee, "Départements", couleurs)
    if "dire2_cam" in value:
        graphs_libre["dire2_cam"] = fig_camembert("DIRE-02", selected_annee, couleurs)
    if "dire3_bat" in value:
        graphs_libre["dire3_bat"] = fig_trim_baton("DIRE-03", selected_annee, "Départements", couleurs)
    if "dire3_cou" in value:
        graphs_libre["dire3_cou"] = fig_trim_courbe("DIRE-03", selected_annee, couleurs)
    if "dire3_tot" in value:
        graphs_libre["dire3_tot"] = fig_annuelle_baton("DIRE-03", selected_annee, "Départements", couleurs)
    if "dire3_cam" in value:
        graphs_libre["dire3_cam"] = fig_camembert("DIRE-03", selected_annee, couleurs)
    #DAF
    if "daf1_bat" in value:
        graphs_libre["daf1_bat"] = fig_trim_baton("DAF-01", selected_annee, "Départements", couleurs)
    if "daf1_cou" in value:
        graphs_libre["daf1_cou"] = fig_trim_courbe("DAF-01", selected_annee, couleurs)
    if "daf1_tot" in value:
        graphs_libre["daf1_tot"] = fig_annuelle_baton("DAF-01", selected_annee, "Départements", couleurs)
    if "daf1_cam" in value:
        graphs_libre["daf1_cam"] = fig_camembert("DAF-01", selected_annee, couleurs)
    if "daf2_bat" in value:
        graphs_libre["daf2_bat"] = fig_trim_baton("DAF-02", selected_annee, "Départements", couleurs)
    if "daf2_cou" in value:
        graphs_libre["daf2_cou"] = fig_trim_courbe("DAF-02", selected_annee, couleurs)
    if "daf2_tot" in value:
        graphs_libre["daf2_tot"] = fig_annuelle_baton("DAF-02", selected_annee, "Départements", couleurs)
    if "daf2_cam" in value:
        graphs_libre["daf2_cam"] = fig_camembert("DAF-02", selected_annee, couleurs)
    if "daf3_bat" in value:
        graphs_libre["daf3_bat"] = fig_trim_baton("DAF-03", selected_annee, "Départements", couleurs)
    if "daf3_cou" in value:
        graphs_libre["daf3_cou"] = fig_trim_courbe("DAF-03", selected_annee, couleurs)
    if "daf3_tot" in value:
        graphs_libre["daf3_tot"] = fig_annuelle_baton("DAF-03", selected_annee, "Départements", couleurs)
    if "daf3_cam" in value:
        graphs_libre["daf3_cam"] = fig_camembert("DAF-03", selected_annee, couleurs)
    if "daf4_bat" in value:
        graphs_libre["daf4_bat"] = fig_trim_baton("DAF-04", selected_annee, "Départements", couleurs)
    if "daf4_cou" in value:
        graphs_libre["daf4_cou"] = fig_trim_courbe("DAF-04", selected_annee, couleurs)
    if "daf4_tot" in value:
        graphs_libre["daf4_tot"] = fig_annuelle_baton("DAF-04", selected_annee, "Départements", couleurs)
    if "daf4_cam" in value:
        graphs_libre["daf4_cam"] = fig_camembert("DAF-04", selected_annee, couleurs)
    if "daf5_bat" in value:
        graphs_libre["daf5_bat"] = fig_trim_baton("DAF-05", selected_annee, "Départements", couleurs)
    if "daf5_cou" in value:
        graphs_libre["daf5_cou"] = fig_trim_courbe("DAF-05", selected_annee, couleurs)
    if "daf5_tot" in value:
        graphs_libre["daf5_tot"] = fig_annuelle_baton("DAF-05", selected_annee, "Départements", couleurs)
    if "daf6_bat" in value:
        graphs_libre["daf6_bat"] = fig_annuelle_baton("DAF-06", selected_annee, "Départements", couleurs)
    if "daf6_cam" in value:
        graphs_libre["daf6_cam"] = fig_camembert("DAF-06", selected_annee, couleurs)
    #DRH
    if "drh1_tot" in value:
        graphs_libre["drh1_tot"] = fig_annuelle_baton("DRH-01", selected_annee, "Services/Départements", couleurs_all)
    if "drh1_cam" in value:
        graphs_libre["drh1_cam"] = fig_camembert("DRH-01", selected_annee, couleurs_all)
    if "drh2_tot" in value:
        graphs_libre["drh2_tot"] = fig_annuelle_baton("DRH-02", selected_annee, "Services/Départements", couleurs_all)
    if "drh2_cam" in value:
        graphs_libre["drh2_cam"] = fig_camembert("DRH-02", selected_annee, couleurs_all)
    if "drh3_bat" in value:
        graphs_libre["drh3_bat"] = fig_trim_baton("DRH-03", selected_annee, "Départements", couleurs)
    if "drh3_cou" in value:
        graphs_libre["drh3_cou"] = fig_trim_courbe("DRH-03", selected_annee, couleurs)
    if "drh3_tot" in value:
        graphs_libre["drh3_tot"] = fig_annuelle_baton("DRH-03", selected_annee, "Départements", couleurs)
    if "drh3_cam" in value:
        graphs_libre["drh3_cam"] = fig_camembert("DRH-03", selected_annee, couleurs)
    if "drh4_tot" in value:
        graphs_libre["drh4_tot"] = fig_annuelle_baton("DRH-04", selected_annee, "Services/Départements", couleurs_all)
    if "drh4_cam" in value:
        graphs_libre["drh4_cam"] = fig_camembert("DRH-04", selected_annee, couleurs_all)
    if "drh5_tot" in value:
        graphs_libre["drh5_tot"] = fig_annuelle_baton("DRH-05", selected_annee, "Services/Départements", couleurs_all)
    if "drh5_cam" in value:
        graphs_libre["drh5_cam"] = fig_camembert("DRH-05", selected_annee, couleurs_all)
    if "drh6_tot" in value:
        graphs_libre["drh6_tot"] = fig_annuelle_baton("DRH-06", selected_annee, "Services/Départements", couleurs_all)
    if "drh6_cam" in value:
        graphs_libre["drh6_cam"] = fig_camembert("DRH-06", selected_annee, couleurs_all)
    #DRI
    if "dri1_bat" in value:
        graphs_libre["dri1_bat"] = fig_trim_baton("DRI-01", selected_annee, "Temps", None)
    if "dri2_bat" in value:
        graphs_libre["dri2_bat"] = fig_trim_baton("DRI-02", selected_annee, "Temps", None)
    if "dri3_bat" in value:
        graphs_libre["dri3_bat"] = fig_trim_baton("DRI-03", selected_annee, "Temps", None)
    if "dri4_bat" in value:
        graphs_libre["dri4_bat"] = fig_trim_baton("DRI-04", selected_annee, "Temps", None)
    if "dri5_bat" in value:
        graphs_libre["dri5_bat"] = fig_trim_baton("DRI-05", selected_annee, "Temps", None)
    if "dri6_tot" in value:
        graphs_libre["dri6_tot"] = fig_annuelle_baton("DRI-06", selected_annee, "", None)
    #ARTEMIS
    if "radar_artemis" in value:
        graphs_libre["radar_artemis"] = fig_radar(selected_annee, 0)
    if "dire1_bat_artemis" in value:
        graphs_libre["dire1_bat_artemis"] = fig_dept_trim_baton("DIRE-01", selected_annee, 0)
    if "dire2_bat_artemis" in value:
        graphs_libre["dire2_bat_artemis"] = fig_dept_trim_baton("DIRE-02", selected_annee, 0)
    if "dire3_bat_artemis" in value:
        graphs_libre["dire3_bat_artemis"] = fig_dept_trim_baton("DIRE-03", selected_annee, 0)
    if "daf1_bat_artemis" in value:
        graphs_libre["daf1_bat_artemis"] = fig_dept_trim_baton("DAF-01", selected_annee, 0)
    if "daf2_bat_artemis" in value:
        graphs_libre["daf2_bat_artemis"] = fig_dept_trim_baton("DAF-02", selected_annee, 0)
    if "daf3_bat_artemis" in value:
        graphs_libre["daf3_bat_artemis"] = fig_dept_trim_baton("DAF-03", selected_annee, 0)
    if "daf4_bat_artemis" in value:
        graphs_libre["daf4_bat_artemis"] = fig_dept_trim_baton("DAF-04", selected_annee, 0)
    if "daf5_bat_artemis" in value:
        graphs_libre["daf5_bat_artemis"] = fig_dept_trim_baton("DAF-05", selected_annee, 0)
    if "drh3_bat_artemis" in value:
        graphs_libre["drh3_bat_artemis"] = fig_dept_trim_baton("DRH-03", selected_annee, 0)
    #CITI
    if "radar_citi" in value:
        graphs_libre["radar_citi"] = fig_radar(selected_annee, 1)
    if "dire1_bat_citi" in value:
        graphs_libre["dire1_bat_citi"] = fig_dept_trim_baton("DIRE-01", selected_annee, 1)
    if "dire2_bat_citi" in value:
        graphs_libre["dire2_bat_citi"] = fig_dept_trim_baton("DIRE-02", selected_annee, 1)
    if "dire3_bat_citi" in value:
        graphs_libre["dire3_bat_citi"] = fig_dept_trim_baton("DIRE-03", selected_annee, 1)
    if "daf1_bat_citi" in value:
        graphs_libre["daf1_bat_citi"] = fig_dept_trim_baton("DAF-01", selected_annee, 1)
    if "daf2_bat_citi" in value:
        graphs_libre["daf2_bat_citi"] = fig_dept_trim_baton("DAF-02", selected_annee, 1)
    if "daf3_bat_citi" in value:
        graphs_libre["daf3_bat_citi"] = fig_dept_trim_baton("DAF-03", selected_annee, 1)
    if "daf4_bat_citi" in value:
        graphs_libre["daf4_bat_citi"] = fig_dept_trim_baton("DAF-04", selected_annee, 1)
    if "daf5_bat_citi" in value:
        graphs_libre["daf5_bat_citi"] = fig_dept_trim_baton("DAF-05", selected_annee, 1)
    if "drh3_bat_citi" in value:
        graphs_libre["drh3_bat_citi"] = fig_dept_trim_baton("DRH-03", selected_annee, 1)
    #EPH
    if "radar_eph" in value:
        graphs_libre["radar_eph"] = fig_radar(selected_annee, 2)
    if "dire1_bat_eph" in value:
        graphs_libre["dire1_bat_eph"] = fig_dept_trim_baton("DIRE-01", selected_annee, 2)
    if "dire2_bat_eph" in value:
        graphs_libre["dire2_bat_eph"] = fig_dept_trim_baton("DIRE-02", selected_annee, 2)
    if "dire3_bat_eph" in value:
        graphs_libre["dire3_bat_eph"] = fig_dept_trim_baton("DIRE-03", selected_annee, 2)
    if "daf1_bat_eph" in value:
        graphs_libre["daf1_bat_eph"] = fig_dept_trim_baton("DAF-01", selected_annee, 2)
    if "daf2_bat_eph" in value:
        graphs_libre["daf2_bat_eph"] = fig_dept_trim_baton("DAF-02", selected_annee, 2)
    if "daf3_bat_eph" in value:
        graphs_libre["daf3_bat_eph"] = fig_dept_trim_baton("DAF-03", selected_annee, 2)
    if "daf4_bat_eph" in value:
        graphs_libre["daf4_bat_eph"] = fig_dept_trim_baton("DAF-04", selected_annee, 2)
    if "daf5_bat_eph" in value:
        graphs_libre["daf5_bat_eph"] = fig_dept_trim_baton("DAF-05", selected_annee, 2)
    if "drh3_bat_eph" in value:
        graphs_libre["drh3_bat_eph"] = fig_dept_trim_baton("DRH-03", selected_annee, 2)
    #INF
    if "radar_inf" in value:
        graphs_libre["radar_inf"] = fig_radar(selected_annee, 3)
    if "dire1_bat_inf" in value:
        graphs_libre["dire1_bat_inf"] = fig_dept_trim_baton("DIRE-01", selected_annee, 3)
    if "dire2_bat_inf" in value:
        graphs_libre["dire2_bat_inf"] = fig_dept_trim_baton("DIRE-02", selected_annee, 3)
    if "dire3_bat_inf" in value:
        graphs_libre["dire3_bat_inf"] = fig_dept_trim_baton("DIRE-03", selected_annee, 3)
    if "daf1_bat_inf" in value:
        graphs_libre["daf1_bat_inf"] = fig_dept_trim_baton("DAF-01", selected_annee, 3)
    if "daf2_bat_inf" in value:
        graphs_libre["daf2_bat_inf"] = fig_dept_trim_baton("DAF-02", selected_annee, 3)
    if "daf3_bat_inf" in value:
        graphs_libre["daf3_bat_inf"] = fig_dept_trim_baton("DAF-03", selected_annee, 3)
    if "daf4_bat_inf" in value:
        graphs_libre["daf4_bat_inf"] = fig_dept_trim_baton("DAF-04", selected_annee, 3)
    if "daf5_bat_inf" in value:
        graphs_libre["daf5_bat_inf"] = fig_dept_trim_baton("DAF-05", selected_annee, 3)
    if "drh3_bat_inf" in value:
        graphs_libre["drh3_bat_inf"] = fig_dept_trim_baton("DRH-03", selected_annee, 3)
    #RS2M
    if "radar_rs2m" in value:
        graphs_libre["radar_rs2m"] = fig_radar(selected_annee, 4)
    if "dire1_bat_rs2m" in value:
        graphs_libre["dire1_bat_rs2m"] = fig_dept_trim_baton("DIRE-01", selected_annee, 4)
    if "dire2_bat_rs2m" in value:
        graphs_libre["dire2_bat_rs2m"] = fig_dept_trim_baton("DIRE-02", selected_annee, 4)
    if "dire3_bat_rs2m" in value:
        graphs_libre["dire3_bat_rs2m"] = fig_dept_trim_baton("DIRE-03", selected_annee, 4)
    if "daf1_bat_rs2m" in value:
        graphs_libre["daf1_bat_rs2m"] = fig_dept_trim_baton("DAF-01", selected_annee, 4)
    if "daf2_bat_rs2m" in value:
        graphs_libre["daf2_bat_rs2m"] = fig_dept_trim_baton("DAF-02", selected_annee, 4)
    if "daf3_bat_rs2m" in value:
        graphs_libre["daf3_bat_rs2m"] = fig_dept_trim_baton("DAF-03", selected_annee, 4)
    if "daf4_bat_rs2m" in value:
        graphs_libre["daf4_bat_rs2m"] = fig_dept_trim_baton("DAF-04", selected_annee, 4)
    if "daf5_bat_rs2m" in value:
        graphs_libre["daf5_bat_rs2m"] = fig_dept_trim_baton("DAF-05", selected_annee, 4)
    if "drh3_bat_rs2m" in value:
        graphs_libre["drh3_bat_rs2m"] = fig_dept_trim_baton("DRH-03", selected_annee, 4)
    #RST
    if "radar_rst" in value:
        graphs_libre["radar_rst"] = fig_radar(selected_annee, 5)
    if "dire1_bat_rst" in value:
        graphs_libre["dire1_bat_rst"] = fig_dept_trim_baton("DIRE-01", selected_annee, 5)
    if "dire2_bat_rst" in value:
        graphs_libre["dire2_bat_rst"] = fig_dept_trim_baton("DIRE-02", selected_annee, 5)
    if "dire3_bat_rst" in value:
        graphs_libre["dire3_bat_rst"] = fig_dept_trim_baton("DIRE-03", selected_annee, 5)
    if "daf1_bat_rst" in value:
        graphs_libre["daf1_bat_rst"] = fig_dept_trim_baton("DAF-01", selected_annee, 5)
    if "daf2_bat_rst" in value:
        graphs_libre["daf2_bat_rst"] = fig_dept_trim_baton("DAF-02", selected_annee, 5)
    if "daf3_bat_rst" in value:
        graphs_libre["daf3_bat_rst"] = fig_dept_trim_baton("DAF-03", selected_annee, 5)
    if "daf4_bat_rst" in value:
        graphs_libre["daf4_bat_rst"] = fig_dept_trim_baton("DAF-04", selected_annee, 5)
    if "daf5_bat_rst" in value:
        graphs_libre["daf5_bat_rst"] = fig_dept_trim_baton("DAF-05", selected_annee, 5)
    if "drh3_bat_rst" in value:
        graphs_libre["drh3_bat_rst"] = fig_dept_trim_baton("DRH-03", selected_annee, 5)
    #Autres
    if "radar_global" in value:
        graphs_libre["radar_global"] = fig_radar_all_dept(selected_annee)

    if value is None:
        value = []



    # Filtrer les graphiques sélectionnés
    selected_graphs = [graph_id for graph_id in value]

    # Générer uniquement les graphiques sélectionnés
    graph_output = [dcc.Graph(figure=graphs_libre[graph_id], config={'displaylogo': False}) for graph_id in selected_graphs]


    new_graph_output = []

    i = 0
    while 2 * i < len(graph_output):
        if (2 * i + 1 < len(graph_output)):

            graph1 = graph_output[2 * i]
            graph2 = graph_output[2 * i + 1]

            new_graph_output.append(
                dbc.Row(children=[
                    dbc.Col(graph1, width=6),
                    dbc.Col(graph2, width=6)
                ])
            )
            new_graph_output.append(
                html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)

        else:
            graph = graph_output[2 * i]
            new_graph_output.append(
                dbc.Row(children=[
                    dbc.Col(graph)
                ])
            )
            new_graph_output.append(
                html.Hr(style={'borderTop': '2px solid #000000'}))  # Ligne horizontale pour mieux séparer les graphes)
        i += 1

    return new_graph_output, {'display': 'none'}