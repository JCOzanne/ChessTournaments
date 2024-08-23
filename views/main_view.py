def display_main_menu():
    print("1. Créer un tournoi")
    print("2. Générer un rapport")
    print("3. Quitter")

    while True:  # Boucle jusqu'à ce que l'utilisateur entre une valeur correcte
        choice = input("Choisissez une option: ")
        if choice.isdigit() and int(choice) in [1, 2, 3]:
            return choice
        else:
            print("Entrée invalide. Veuillez entrer un chiffre correspondant à une option.")
