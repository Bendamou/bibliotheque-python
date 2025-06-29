class Livre:
    def __init__(self, isbn, titre, auteur, annee, genre):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.statut = "indisponible"

    def __str__(self):
        return f"LIVRE (ISBN: {self.isbn} | Titre: {self.titre} | Auteur: {self.auteur} | Statut: {self.statut})"
    def __repr__(self):
        return f"\nLIVRE (ISBN: {self.isbn} | Titre: {self.titre} | Auteur: {self.auteur} | Statut: {self.statut})"

