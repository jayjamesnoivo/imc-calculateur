from interface import *
from calculs import *
from historique import *

def main(poids:float=None, taille:float=None):
    '''
    Si on entre aucun paramètre à l'appel de la fonction, on demande un input
    de l'utilisateur.

    :param poids: Description
    :type poids: float
    :param taille: Description
    :type taille: float
    '''
    if poids is None or taille is None:
        poids, taille = demander_infos()

    imc = calculer_imc(poids, taille)
    categorie = interpreter_imc(imc)
    afficher_resultat(imc, categorie)

    sauvegarde_calcul = input("Est-ce que vous voulez enregistrer votre résultat (y/n)? ")
    if sauvegarde_calcul == "y":
        print("\n")
        sauvegarder_calcul(input("Votre nom: "), imc)

    affichage_historique = input("Est-ce que vous voulez voir les résultats de l'historique (y/n)? ")
    if affichage_historique == "y":
        print("\n")
        afficher_historique()

def test_imc():
    '''
    Appel main avec plusieurs valeur de poids.
    Test tout les catégories de imc
    '''
    main(poids=50, taille=1.75)  # Insuffisance pondérale
    main(poids=65, taille=1.75)  # Poids normal
    main(poids=80, taille=1.75)  # Surpoids
    main(poids=95, taille=1.75)  # Obésité

if __name__ == "__main__":
    test_imc()
    main()