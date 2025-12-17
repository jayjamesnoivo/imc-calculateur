def demander_infos():
    while True:
        try: # Try/except pour forcer une entrée de donnée valide (pas de négatif ou de texte), sinon erreur
            poids = float (input("Entrez votre poids (kg) : "))
            if poids <= 0:
                print("Le poids doit être supérieur à 0.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour le poids.")

    while True:
        try:
            taille = float (input("Entrez votre taille (m) : ")) #Float pour conserver les décimales
            if taille <= 0:
                print("La taille doit être supérieure à 0.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour la taille.")

    return poids, taille

def afficher_resultat (imc, categorie):
    print("\n==== Résultat ====")
    print(f"IMC : {imc:.2f}")
    print(f"Catégorie : {categorie}")