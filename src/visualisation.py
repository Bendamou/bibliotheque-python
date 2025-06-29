import matplotlib.pyplot as plt
import random

#----------------Livre--------------
couleurs = [
        '#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', '#ffcc00',
        '#66c2a5', '#fc8d62', '#8da0cb', '#a6d854', '#ffd92f', '#e78ac3',
        '#b3b3b3', '#cab2d6', '#ffff99', '#1f78b4', '#33a02c', '#fb9a99',
        '#fdbf6f', '#b15928', '#ffb347', '#87ceeb', '#dda0dd', '#90ee90', '#fa8072'
    ]

def visualiser_par_genre(livres):
    genre_counts = {}

    # Compter les livres valides par genre
    for info in livres.values():
        livre = info["livre"]
        genre = livre.genre
        quantite = info["quantite"]

        if info.get("est_supprimer", "False") == "False" and quantite != 0:
            genre_counts[genre] = genre_counts.get(genre, 0) + quantite

    # Cas où aucun livre valide n'existe
    if not genre_counts:
        genre_counts = {"aucun livre": 100}

    # Si plus de 10 genres, prendre 9 plus grands + "Autres"
    if len(genre_counts) > 9:
        sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
        top_9 = sorted_genres[:8]
        autres = sorted_genres[8:]
        autres_total = sum(q for _, q in autres)
        top_genres = top_9 + [(f"Autre", autres_total)]
    else:
        top_genres = genre_counts.items()

    # Mélanger les éléments pour désordonner visuellement
    items = list(top_genres)
    random.shuffle(items)

    # Séparer labels et valeurs
    labels = [label for label, _ in items]
    sizes = [size for _, size in items]


    random.shuffle(couleurs)

    # Affichage du graphique
    

    plt.figure(figsize=(12, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=couleurs[:len(labels)], startangle=120)
    plt.title("Répartition des Livres par Genre", pad=40)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

def visualiser_par_quantite_max(livres):

    # Extraire les livres valides (non supprimés)
    livres_valides = [
        (info["livre"].titre, info["quantite"])
        for info in livres.values()
        if info.get("est_supprimer", "False") == "False"
    ]

    # Trier par quantité décroissante
    livres_valides.sort(key=lambda x: x[1], reverse=True)

    # Limiter à 25 livres maximum
    livres_valides = livres_valides[:25]

    # Extraire titres et quantités
    titres = [titre for titre, _ in livres_valides]
    quantites = [quantite for _, quantite in livres_valides]

    # Mélanger les couleurs dans l’ordre des livres
    couleurs_dispo = couleurs[:len(titres)]
    random.shuffle(couleurs_dispo)

    # Paramètres de style
    plt.rcParams.update({
        "figure.figsize": (12, 8),
        "axes.facecolor": "#f8f8f8",
        "axes.labelcolor": "black",
        "axes.titlesize": 20,
        "xtick.color": "#000000",
        "ytick.color": "#000000",
        "font.size": 10,
    })

    # Affichage du graphique
    plt.bar(titres, quantites, color=couleurs_dispo)
    plt.xlabel("Titre du Livre", labelpad=15)
    plt.ylabel("Quantité Disponible", labelpad=20)
    plt.title("Les Livres les plus Disponibles", pad=25)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def visualiser_par_quantite_min(livres):

    # Extraire les livres valides (non supprimés)
    livres_valides = [
        (info["livre"].titre, info["quantite"])
        for info in livres.values()
        if info.get("est_supprimer", "False") == "False"
    ]

    # Trier par quantité **croissante**
    livres_valides.sort(key=lambda x: x[1])

    # Limiter à 25 livres minimum
    livres_valides = livres_valides[:25]

    # Extraire titres et quantités
    titres = [titre for titre, _ in livres_valides]
    quantites = [quantite for _, quantite in livres_valides]

    # Couleurs (aléatoirement)
    couleurs_dispo = couleurs[:len(titres)]
    random.shuffle(couleurs_dispo)

    # Style matplotlib
    plt.rcParams.update({
        "figure.figsize": (12, 8),
        "axes.facecolor": "#f8f8f8",
        "axes.labelcolor": "black",
        "axes.titlesize": 20,
        "xtick.color": "#000000",
        "ytick.color": "#000000",
        "font.size": 10,
    })

    # Affichage du graphique
    plt.bar(titres, quantites, color=couleurs)
    plt.xlabel("Titre du Livre", labelpad=15)
    plt.ylabel("Quantité Disponible", labelpad=20)
    plt.title("Les Livres les Moins Disponibles", pad=25)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def visualiser_meilleurs_livres_empruntes(Top_15_livres,livres):
    
    titres = []
    emprunts = []

    for isbn, nombre_emprunts in Top_15_livres:
        titres.append(livres[isbn]["livre"].titre)
        emprunts.append(nombre_emprunts)

    plt.rcParams.update({
        "figure.figsize": (12, 8),
        "axes.facecolor": "#f5f5f5",
        "axes.labelcolor": "black",
        "axes.titlesize": 20,
        "xtick.color": "#000000",
        "ytick.color": "#000000",
        "font.size": 10,
    })


    plt.bar(titres, emprunts, color=couleurs[:len(titres)])
    plt.xlabel("Titres des Livres", labelpad=15)
    plt.ylabel("Nombre d'Emprunts", labelpad=20)
    plt.title("Top des Livres les Plus Empruntés", pad=25)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

#----------------Membre é Author------------

def visualiser_membres_plus_actifs(membres, top_n=15):

    # Construction de la liste des membres et nombre d'emprunts
    emprunts_par_membre = [
        (info["membre"].nom, len(info.get("historique_livre_emprunte", [])))
        for info in membres.values()
    ]

    # Trier par ordre décroissant du nombre d'emprunts
    emprunts_par_membre.sort(key=lambda x: x[1], reverse=True)

    # Prendre les top N membres
    top = emprunts_par_membre[:top_n]

    # Séparer les noms et les nombres d'emprunts
    noms = [nom for nom, count in top]
    nb_emprunts = [count for _, count in top]
    # Affichage du graphique
    plt.figure(figsize=(12, 6))
    plt.bar(noms, nb_emprunts, color = couleurs)
    plt.title("Top Membres les Plus Actifs", pad=20)
    plt.xlabel("Nom du Membre")
    plt.ylabel("Nombre Total d'Emprunts")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def visualiser_auteurs_plus_populaires(Top_15_livres,livres):
    titres = []
    emprunts = []

    for isbn, nombre_emprunts in Top_15_livres:
        titres.append(livres[isbn]["livre"].auteur)
        emprunts.append(nombre_emprunts)

    plt.rcParams.update({
        "figure.figsize": (12, 8),
        "axes.facecolor": "#f5f5f5",
        "axes.labelcolor": "black",
        "axes.titlesize": 20,
        "xtick.color": "#000000",
        "ytick.color": "#000000",
        "font.size": 10,
    })


    plt.bar(titres, emprunts, color=couleurs[:len(titres)])
    plt.title("Top des Auteurs les Plus Populaires", pad=20)
    plt.xlabel("Auteur")
    plt.ylabel("Nombre total d'emprunts")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()