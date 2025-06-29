class Membre:
    def __init__(self, identifiant, nom):
        self.identifiant = identifiant
        self.nom = nom
        self.livres_empruntes = []

    def emprunter(self, livre):
           self.livres_empruntes.append(livre)

    def rendre(self, livre):
            self.livres_empruntes.remove(livre)

    def __str__(self):
        return f"{self.identifiant} - {self.nom} : \n-->livre_emprunte :{self.livres_empruntes}"