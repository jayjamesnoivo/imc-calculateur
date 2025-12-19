def sauvegarder_calcul(nom, imc):
    with open("sauvegarde_calcul.txt", "a") as fichier:
        fichier.write(f"{nom}: {imc} \n")

def afficher_historique():
    with open("sauvegarde_calcul.txt", "r") as fichier:
        contenu = fichier.read()
        print(f"Historique:\n{contenu}")
