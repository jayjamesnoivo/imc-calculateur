def calculer_imc(poids, taille):
    """
    Calcule l'IMC à partir du poids (kg) et de la taille (m).
    """
    if poids <= 0:
        raise ValueError("Le poids doit être supérieur à 0.")
    if taille <= 0:
        raise ValueError("La taille doit être supérieure à 0.")

    imc = poids / (taille ** 2)
    return round(imc, 2)


def interpreter_imc(imc):
    """
    Retourne la catégorie associée à un IMC.
    """
    if imc < 18.5:
        return "Insuffisance pondérale"
    elif imc < 25:
        return "Poids normal"
    elif imc < 30:
        return "Surpoids"
    else:
        return "Obésité"
