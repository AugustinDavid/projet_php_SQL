import read_action
import insert_action
# import update_action
import delete_action

def main():

    print("""
        Bienvenue à l'herboristerie CHINCHAN du CAMPUS
        Veulliez choisir une option à effectuer
        L : pour lister les produits du magasin
        A : pour ajouter un produit
        S : pour supprimer
        """)
    
    # liste_repertoire = repertoire_action.get_rep()
    
    
    while True:
    
        saisie_utilisateur = str(input("Choisissez une option"))
    
        if saisie_utilisateur.upper() == 'L':
            read_action.read()
           
    
        elif saisie_utilisateur.upper() == 'A':
            insert_action.insert()
            print("""Base de donnée mise à jour
                  L'entrée à bien été ajouter""")
    
        elif saisie_utilisateur.upper() == 'S':
            delete_action.delete()
            print("l'entrée à été supprimé du catalogue")
            read_action.read()
    
        # if saisie_utilisateur.upper() == 'M':
        #     plante = update_action.update()
        #     print(plante)
    
        if saisie_utilisateur.upper() == 'Q':
            break

main()