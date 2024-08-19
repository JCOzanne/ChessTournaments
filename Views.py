from Models import Player
from datetime import datetime


class MainMenuView:

    def display_menu(self):
        print("\n--- Menu Principal ---")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Renseigner les tours")
        print("4. Générer un rapport")
        print("0. Quitter")

    def get_user_choice(self):
        return input("Choisissez une option : ")

    def display_message(self, message):
        print(message)


class PlayerView:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_player_info(self):
        print("\n--- Ajouter un Joueur ---")
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        birthday = input("Date de naissance (JJ-MM-AAAA) : ")
        national_chess_id = input("Numéro national d'échecs : ")
        rating = int(input("Évaluation : "))
        player = Player(first_name, last_name, birthday, national_chess_id, rating)
        self.players.append(player)

    def display_players(self):
        for player in sorted(self.players, key=lambda p: (p.last_name, p.first_name)):
            print(player)


class RoundView:

    def __init__(self):
        self.rounds = []

    def get_round_name(self):
        return input("Nom du tour (ex: Round 1) : ")

    def display_round_info(self, round):
        print(f"\n--- {round.name} ---")
        print(f"Début : {round.start_date}")
        for match in round.matches:
            print(match)

    def mark_round_as_finished(self, round):
        confirmation = input(f"Marquer le {round.name} comme terminé ? (oui/non) : ")
        if confirmation.lower() == "oui":
            round.end_date = datetime.now()
            print(f"{round.name} terminé à {round.end_date}")


class TournamentView:

    def get_tournament_info(self):
        print("\n--- Créer un Tournoi ---")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début (JJ-MM-AAAA) : ")
        end_date = input("Date de fin (JJ-MM-AAAA) : ")
        description = input("Description : ")
        return name, location, start_date, end_date, description

    def select_players(self, all_players):
        selected_players = []
        print("\n--- Sélection des joueurs ---")
        for i, player in enumerate(all_players):
            print(f"{i + 1}. {player}")
        print("0. Terminer la sélection")

        while True:
            choice = int(input("Sélectionnez un joueur (0 pour terminer) : "))
            if choice == 0:
                break
            if 0 < choice <= len(all_players):
                selected_players.append(all_players[choice - 1])
        return selected_players

    class RapportView:

        def display_tournament_report(self, tournament):
            print(f"\n--- Rapport du Tournoi : {tournament.name} ---")
            print(f"Lieu : {tournament.location}")
            print(f"Date de début : {tournament.start_date}")
            print(f"Date de fin : {tournament.end_date}")
            print("\nListe des joueurs (par ordre alphabétique) :")
            sorted_players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
            for player in sorted_players:
                print(player)

            # Appel à la méthode déplacée ici
            self.display_rounds_and_matches(tournament.rounds)

        def display_rounds_and_matches(self, rounds):
            print("\n--- Liste des Tours et des Matchs ---")
            for round in rounds:
                print(f"Tour : {round.name}, Début : {round.start_date}, Fin : {round.end_date}")
                for match in round.matches:
                    print(f"{match.player1} vs {match.player2}")





