import dash
from dash import html

dash.register_page(
    __name__,
    title = "A propos",
    name = "a-propos",
    order=17,
    active= False
                   )

layout = html.Div([
    html.H1("À propos"),
    html.P("Cette application a été développée en 2023 par JACQUET Marin et CAILLARD Mathias, deux étudiants en 2ème année à Télécom SudParis. Le projet a été encadré par Bruno DEFUDE par Benoît JEAN dans le cadre d'un 'projet Cassiopée'."),
    html.H2("Contact : "),
    html.A("marin.jacquet@telecom-sudparis.com", href="mailto:marin.jacquet@telecom-sudparis.eu"),
    html.Br(),
    html.A("mathias.caillard@telecom-sudparis.com", href="mailto:mathias.caillard@telecom-sudparis.eu"),
    html.Br(),
    html.Br(),
    html.H2("Manuel d'utilisateur"),
    html.P("Cette application est un outil de visualisation des indicateurs de suivi de Télécom SudParis."),
    html.P("Dans les onglets des Directions de l'école (DF, DRFD, DAF, DRH, DRI), vous pouvez visualiser divers indicateurs produits par les Directions associés." ),
    html.P("Dans le menu déroulant 'Département', vous pouvez sélectionner un département et visualiser divers indicateurs qui concernent le département associée. "),
    html.P("Dans l'onglet 'Options', vous pouvez sélectionner l'année des données des indicateurs qui vous intéresse."),
    html.P("Dans l'onglet 'Historique', vous pouvez choisir et sélectionner (à l'aide d'un moteur de recherche) vos indicateurs à la carte, pour une visualisation et comparaison personnalisées."),
    html.P("Pour un graphique donnée, vous pouvez sélectionner les composantes qui vous souhaitez afficher en cliquant sur le symbole correspondant dans la légende. Un double-clique permet de ne sélectionner seulement la composante désirée. Si vous souhaitez enregistrer la figure au format png, cliquez sur sur le logo 'appareil photo'."),
    html.P("L'application exploite des données sous forme de fichiers Excels. Vous pouvez télécharger ces fichiers dans l'onglet 'Options'.")

    ])