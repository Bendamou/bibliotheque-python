# 📚 Système de Gestion de Bibliothèque - Python

Bienvenue dans mon projet de système de gestion de bibliothèque, une application robuste développée en Python avec une interface utilisateur graphique (GUI) intuitive grâce à `Tkinter`. Ce projet a été réalisé dans le cadre d’un mini-projet académique.

---

🧑 **Réalisé par :**
**Mohammed BENDAMOU** 
Filière : Génie Informatique 
Année : 2024/2025

---

🎯 **Objectif du projet :**
Créer une application de bureau complète et facile à utiliser pour la gestion des opérations d'une bibliothèque, incluant la gestion des livres, des membres, ainsi que le suivi des emprunts et des retours.

---

🛠 **Fonctionnalités principales :**

-   **Gestion des Livres :**
    -   Ajout de nouveaux livres avec des détails complets (ISBN, titre, auteur, année, genre, quantité).
    -   Suppression logique des livres (le livre est marqué comme "supprimé" pour conserver l'historique mais n'est plus disponible à l'emprunt).
    -   Mise à jour des quantités de livres existants.
    -   Recherche avancée de livres par divers critères (ISBN, titre, auteur, année, genre).
    -   Affichage clair de l'inventaire des livres.

-   **Gestion des Membres :**
    -   Ajout et suppression de membres.
    -   Recherche de membres par identifiant ou nom.
    -   Affichage de la liste des membres inscrits.
    -   Suivi en temps réel des livres empruntés par chaque membre.
    -   Historique détaillé de tous les livres empruntés par un membre.

-   **Gestion des Emprunts et Retours :**
    -   Processus d'emprunt sécurisé avec vérification de la disponibilité et gestion des copies multiples.
    -   Enregistrement des retours de livres.

-   **Persistance des Données :**
    -   Sauvegarde et chargement automatiques de toutes les données (livres et membres) via des fichiers **JSON**, assurant la conservation des informations entre les sessions.

-   **Visualisations Graphiques :**
    -   Génération de graphiques pertinents via `Matplotlib` pour analyser l'activité de la bibliothèque :
        -   Répartition des livres par genre.
        -   Top des livres les plus/moins disponibles.
        -   Top des membres les plus actifs.
        -   Top des auteurs les plus populaires (basé sur les emprunts).

---

🖼 **Interface Utilisateur (Tkinter) :**
L'application est dotée d'une interface graphique conviviale, permettant une navigation facile et une interaction intuitive avec le système. Elle comprend différentes sections dédiées à la gestion des livres, des membres, des emprunts/retours et des visualisations.

---

📦 **Structure du projet :**

.
├── data/
│   ├── livres.json             # Données des livres sauvegardées
│   └── membres.json            # Données des membres sauvegardées
├── bibliotheque.py             # Logique principale de la bibliothèque (gestion des collections, emprunts, retours, persistance)
├── exceptions.py               # Classes d'exceptions personnalisées
├── livre.py                    # Définition de la classe Livre
├── main.py                     # Point d'entrée de l'application GUI (Tkinter)
├── membre.py                   # Définition de la classe Membre
├── visualisation.py            # Fonctions pour la génération des graphiques (Matplotlib)
└── README.md                   # Ce fichier


---

💡 **Architecture et Conception :**
Le projet est conçu de manière modulaire, séparant la logique métier (classes `Livre`, `Membre`, `Bibliotheque`) de l'interface utilisateur (`main.py`) et des outils auxiliaires (`exceptions.py`, `visualisation.py`). Bien qu'il n'y ait pas de dossiers `model`/`view`/`controller` explicites, cette séparation des responsabilités s'aligne sur les principes d'une architecture propre.

---

🔧 **Technologies utilisées :**
-   **Python 3.x**
-   **Tkinter** (pour l'interface graphique)
-   **JSON** (pour le stockage des données)
-   **Matplotlib** (pour les statistiques et visualisations graphiques)
-   **Git + GitHub** (recommandé pour la gestion de version si ce n'est pas déjà le cas)

---

✅ **Lancer l’application :**

1.  **Prérequis :** Assurez-vous d'avoir Python 3.x installé.
2.  **Installation des dépendances :**
    Ouvrez votre terminal ou invite de commande et exécutez :
    ```bash
    pip install matplotlib
    ```
3.  **Création du dossier de données :**
    Naviguez jusqu'à la racine de votre projet et créez un dossier nommé `data` :
    ```bash
    mkdir data
    ```
    (Les fichiers `livres.json` et `membres.json` seront créés automatiquement à l'intérieur de ce dossier lors de la première sauvegarde.)
4.  **Exécuter l'application :**
    Depuis la racine de votre projet, lancez le script principal :
    ```bash
    python main.py
    ```

---

📌 **Améliorations possibles :**
-   Migration de la persistance des données vers une base de données (ex: SQLite pour un fichier local, ou MySQL/PostgreSQL pour une solution plus robuste).
-   Amélioration de l'interface utilisateur avec des bibliothèques plus modernes ou des thèmes Tkinter avancés.
-   Mise en place d'un système d'authentification des utilisateurs avec différents rôles (administrateur, bibliothécaire, utilisateur simple).
-   Fonctionnalités d'exportation des rapports et statistiques (ex: PDF, CSV).
-   Ajout d'une gestion des utilisateurs.
-   Gestion des pénalités pour les retours tardifs.

---

📃 **Licence :**
Ce projet est libre et peut être réutilisé à des fins éducatives.

---
