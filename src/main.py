class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.emprunte = False

    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee}) {'[Emprunté]' if self.emprunte else '[Disponible]'}"


class Bibliotheque:
    def __init__(self):
        self.catalogue = []

    def ajouter_livre(self, livre):
        if not any(
            a.titre == livre.titre and a.auteur == livre.auteur for a in self.catalogue
        ):
            self.catalogue.append(livre)
            return True
        return False

    def retirer_livre(self, titre):
        for livre in self.catalogue:
            if livre.titre == titre:
                self.catalogue.remove(livre)
                return True
        return False

    def emprunter_livre(self, titre):
        for livre in self.catalogue:
            if livre.titre == titre and not livre.emprunte:
                livre.emprunte = True
                return True
        return False

    def retourner_livre(self, titre):
        for livre in self.catalogue:
            if livre.titre == titre and livre.emprunte:
                livre.emprunte = False
                return True
        return False

    def rechercher_livre(self, titre):
        return [
            livre for livre in self.catalogue if titre.lower() in livre.titre.lower()
        ]

    def afficher_catalogue(self):
        return [str(livre) for livre in self.catalogue]


# Exemple d'utilisation
if __name__ == "__main__":
    biblio = Bibliotheque()

    livre1 = Livre("1984", "George Orwell", 1949)
    livre2 = Livre("Le Meilleur des Mondes", "Aldous Huxley", 1932)
    livre3 = Livre("Fahrenheit 451", "Ray Bradbury", 1953)

    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_livre(livre3)

    print("Catalogue initial:")
    print("\n".join(biblio.afficher_catalogue()))

    biblio.emprunter_livre("1984")
    print("\nCatalogue après emprunt de '1984':")
    print("\n".join(biblio.afficher_catalogue()))

    biblio.retourner_livre("1984")
    print("\nCatalogue après retour de '1984':")
    print("\n".join(biblio.afficher_catalogue()))
