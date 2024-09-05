def display_main_menu():
    print("1. Créer un tournoi")
    print("2. Générer un rapport")
    print("3. Revenir où je me suis arrêté")
    print("4. Quitter")

    while True:
        choice = input("Choisissez une option: ")
        if choice.isdigit() and int(choice) in [1, 2, 3, 4]:
            return choice
        else:
            print("Entrée invalide. Veuillez entrer un chiffre correspondant à une option.")
