""" La classe livre permet de recenser tous les livres disponibles """
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.emprunte = False
""" Cette fonction permet de savoir si le livre est emprute ou disponible"""
    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee}) {'[Emprunté]' if self.emprunte else '[Disponible]'}"

""" La classe bibliothèque permet de gérer l'emprunt et le retour des livres """
class Bibliotheque:
    def __init__(self):
        self.catalogue = []
"""Ajout d'un livre parmis ceux qui sont dans la bibliothèque"""
    def ajouter_livre(self, livre):
        if not any(
            a.titre == livre.titre and a.auteur == livre.auteur for a in self.catalogue
        ):
            self.catalogue.append(livre)
            return True
        return False
"""Retrait de livre dans la bibliothèque"""
    def retirer_livre(self, titre):
        for livre in self.catalogue:
            if livre.titre == titre:
                self.catalogue.remove(livre)
                return True
        return False
"""Emprunt de livre à la bibliothèque"""
    def emprunter_livre(self, titre):
        for livre in self.catalogue:
            if livre.titre == titre and not livre.emprunte:
                livre.emprunte = True
                return True
        return False
"""Retourner le(s) livre(s)"""
    def retourner_livre(self, titre):
        for livre in self.catalogue:
            if livre.titre == titre and livre.emprunte:
                livre.emprunte = False
                return True
        return False
""" Pour chercher un livre dans le catalogue """
    def rechercher_livre(self, titre):
        return [
            livre for livre in self.catalogue if titre.lower() in livre.titre.lower()
        ]
""" Afficher le catalogue"""
    def afficher_catalogue(self):
        return [str(livre) for livre in self.catalogue]
