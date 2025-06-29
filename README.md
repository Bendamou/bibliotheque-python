
# 📚 Application de Gestion de Bibliothèque - Python

Bienvenue dans le projet LibManage, une application de gestion de bibliothèque développée en Python avec une interface graphique Tkinter. Ce projet a été réalisé dans le cadre d’un mini-projet académique.

🧑 Réalisé par :
Mohammed BENDAMOU  
Filière : Génie Informatique  
Année : 2024/2025

🎯 Objectif du projet :
Créer une application de bureau permettant au personnel d’une bibliothèque de gérer les membres, les livres (et leurs exemplaires), ainsi que les emprunts/retours.

🛠 Fonctionnalités principales :
- Ajouter, rechercher, supprimer des membres
- Enregistrer des livres avec gestion d’exemplaires (ISBN, copy_id, etc.)
- Gérer les emprunts et retours
- Visualiser des statistiques graphiques (via Matplotlib)
- Sauvegarde des données en XML
- Menu contextuel via clic droit pour interactions rapides
- Navigation fluide via un menu latéral

🖼 Interface Utilisateur :
L’interface a été développée avec Tkinter. Elle comprend :
- Un menu de navigation latéral
- Une vue d’accueil avec des statistiques
- Des interfaces dédiées aux livres, membres et emprunts
- Des dialogues contextuels pour les actions rapides

📦 Structure du projet :

project_academique/
├── controller/
├── model/
├── view/
├── data/
│   ├── livres.xml
│   ├── membres.xml
│   └── emprunts.xml
├── main.py
└── README.md

💡 Architecture utilisée : MVC
Le projet est structuré selon le modèle MVC :
- Model : gestion des données (livres, membres, emprunts)
- View : interface graphique
- Controller : interactions utilisateur / logique métier

🔧 Technologies utilisées :
- Python 3.x
- Tkinter (interface graphique)
- XML (stockage des données)
- Matplotlib (graphique/statistiques)
- Git + GitHub (gestion de version)

✅ Lancer l’application :
1. Cloner le dépôt :
   git clone https://github.com/Bendamou/bibliotheque-python.git
   cd bibliotheque-python

2. Exécuter :
   python main.py

📌 Améliorations possibles :
- Migration vers une base de données (SQLite ou MySQL)
- Interface plus moderne (Tkinter avancé ou PyQt)
- Authentification des utilisateurs (admin, bibliothécaire, etc.)
- Exportation des statistiques (PDF, Excel)

📃 Licence :
Ce projet est libre et peut être réutilisé à des fins éducatives.
