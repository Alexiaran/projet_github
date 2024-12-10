import pytest
from library_management import Livre, Bibliotheque

@pytest.fixture
def bibliotheque():
    biblio = Bibliotheque()
    livre1 = Livre("1984", "George Orwell", 1949)
    livre2 = Livre("Le Meilleur des Mondes", "Aldous Huxley", 1932)
    livre3 = Livre("Fahrenheit 451", "Ray Bradbury", 1953)

    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_livre(livre3)
    return biblio

def test_ajouter_livre(bibliotheque):
    livre_nouveau = Livre("Dune", "Frank Herbert", 1965)
    assert bibliotheque.ajouter_livre(livre_nouveau) is True
    assert len(bibliotheque.catalogue) == 4

def test_retirer_livre(bibliotheque):
    assert bibliotheque.retirer_livre("1984") is True
    assert len(bibliotheque.catalogue) == 2
    assert bibliotheque.retirer_livre("Livre Inexistant") is False

def test_emprunter_livre(bibliotheque):
    assert bibliotheque.emprunter_livre("1984") is True
    livre = next(l for l in bibliotheque.catalogue if l.titre == "1984")
    assert livre.emprunte is True
    assert bibliotheque.emprunter_livre("1984") is False  # Déjà emprunté

def test_retourner_livre(bibliotheque):
    bibliotheque.emprunter_livre("1984")
    assert bibliotheque.retourner_livre("1984") is True
    livre = next(l for l in bibliotheque.catalogue if l.titre == "1984")
    assert livre.emprunte is False
    assert bibliotheque.retourner_livre("1984") is False  # Déjà retourné

def test_rechercher_livre(bibliotheque):
    resultats = bibliotheque.rechercher_livre("1984")
    assert len(resultats) == 1
    assert resultats[0].titre == "1984"

def test_afficher_catalogue(bibliotheque):
    catalogue = bibliotheque.afficher_catalogue()
    assert len(catalogue) == 3
    assert "1984 par George Orwell (1949) [Disponible]" in catalogue