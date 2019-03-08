from read import *
from insert import *
from update import *
from delete import *

print("""
    Bienvenue à l'herboristerie CHINCHAN du CAMPUS
    Veulliez choisir une option à effectuer
    L : pour lister les produits du magasin
    A : pour ajouter un produit
    S : pour supprimer
    R : pour rechercher un nom
    """)

# liste_repertoire = repertoire_action.get_rep()


while True:

    saisie_utilisateur = str(input("Choisissez une option"))

    if saisie_utilisateur.upper() == 'L':
        read_action.read()
        for x in myresult:
            print(x)

    elif saisie_utilisateur.upper() == 'A':
        nom_perso = input("Entrez le nom à ajouter")
        phone_perso = input("Entrez le numéro de téléphone")
        adresse_personne = input("Entrez l'adresse")
        repertoire_action.ajouter_personne(liste_repertoire, nom_perso, phone_perso,
                                           adresse_personne)
        print("Le contact à bien été ajouter")

    elif saisie_utilisateur.upper() == 'S':
        nom_a_supprim = input("Quel personne voulez-vous supprimer de l'annuaire ?"
                              " (nom,prenom,numeros)")
        repertoire_action.supprimer_personne(liste_repertoire, nom_a_supprim)
        print("le contact à été supprimé du repertoire")
        print(liste_repertoire)

    if saisie_utilisateur.upper() == 'R':
        recherche_nom = input("Rechercher depuis nom [laisser vide pour ignorer] : ")
        recherche_tel = input("Rechercher depuis numéro [laisser vide pour ignorer] : ")
        recherche_adresse = input("Rechercher depuis adresse [laisser vide pour ignorer] : ")
        contact = repertoire_action.recherche_annuaire(liste_repertoire, recherche_nom,
                                                       recherche_tel, recherche_adresse)
        print(contact)

    if saisie_utilisateur.upper() == 'Q':
        break
