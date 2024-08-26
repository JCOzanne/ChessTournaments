from datetime import datetime
from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from utils.data_manager import load_tournaments, save_tournaments, load_players, save_players


def create_tournament():
    """
    :return: create tournament and update tournaments list
    """
    name = input("Nom du tournoi: ")
    location = input("Lieu du tournoi: ")
    start_date = input("Date de début (JJ-MM-AAAA): ")
    end_date = input("Date de fin (JJ-MM-AAAA): ")
    rounds = int(input("Nombre de tours (par défaut 4): ") or 4)
    description = input("Description: ")
    tournament = Tournament(name, location, start_date, end_date, rounds, description=description)
    tournaments = load_tournaments()
    tournaments.append(tournament)
    save_tournaments(tournaments)
    print("Tournoi créé avec succès!")
    add_players_to_tournament(tournament)
    manage_rounds(tournament)


def get_yes_no(prompt):

    """
    :param prompt:
    :return: a message if the keyboard input is incorrect
    """
    while True:
        response = input(prompt).lower()
        if response in ["oui", "non"]:
            return response
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")


def validate_national_id(national_id):
    """
    :param national_id:
    :return: a message if the national_id is incorrect
    """
    if len(national_id) != 7:
        print("L'identifiant national doit contenir exactement 7 caractères.")
        return False

    if not national_id[:2].isalpha():
        print("Les deux premiers caractères doivent être des lettres.")
        return False

    if not national_id[2:].isdigit():
        print("Les cinq derniers caractères doivent être des chiffres.")
        return False

    return True


def add_players_to_tournament(tournament):
    """
    :param tournament:
    :return: create, load player and save the players.json and tournaments.json files
    """
    while True:
        choice = get_yes_no("Voulez-vous ajouter un joueur au tournoi? (oui/non): ")
        if choice == "non":
            break
        last_name = input("Nom de famille: ")
        first_name = input("Prénom: ")
        birth_date = input("Date de naissance (JJ-MM-AAAA): ")

        while True:
            national_id = input("Identifiant national d'échecs (2 lettres suivies de 5 chiffres): ")
            if validate_national_id(national_id):
                break
        player = Player(last_name, first_name, birth_date, national_id)
        tournament.players_list.append(player)

        # Ajouter le joueur à la liste globale des joueurs
        players = load_players()
        players.append(player)
        save_players(players)

        save_tournaments([tournament])
        print("Joueur ajouté avec succès!")


def manage_rounds(tournament):
    """
    :param tournament:
    :return: create round and add it to tournament, generate matches and save their results, close de round
    """
    for round_num in range(1, tournament.rounds + 1):
        round_name = input(f"Nom de la ronde {round_num}: ")
        round = Round(round_name, tournament, start_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        tournament.rounds_list.append(round)
        save_tournaments([tournament])
        print(f"Date et heure de début de la ronde {round_num}: {round.start_time}")

        # Générer les matchs pour la ronde
        generate_matches(tournament, round)

        # Demander les résultats des matchs
        enter_match_results(round)

        # Marquer la ronde comme terminée
        round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tournaments([tournament])
        print(f"Date et heure de fin de la ronde {round_num}: {round.end_time}")

        # Passer à la ronde suivante
        if round_num < tournament.rounds:
            choice = input("Voulez-vous passer à la ronde suivante? (oui/non): ").lower()
            if choice == "non":
                break


def generate_matches(tournament, round):
    """
    :param tournament:
    :param round:
    :return:generate matches according to the specificities for each round and update tournaments list
    """
    players = sorted(tournament.players_list, key=lambda p: p.points, reverse=True)
    matches = []
    for i in range(0, len(players), 2):
        if i + 1 < len(players):
            match = Match(players[i], players[i + 1])
            matches.append(match)
    round.matches = matches
    save_tournaments([tournament])


def enter_match_results(round):
    """
    :param round:
    :return: Allow user to enter match results ans update tournament list
    """
    for match in round.matches:
        print(
            f"Match entre {match.player1.last_name} {match.player1.first_name} et "
            f"{match.player2.last_name} {match.player2.first_name}")
        result = input("Résultat du match (1-0, 0-1, 0.5-0.5): ")
        if result == "1-0":
            match.score1 = 1
            match.score2 = 0
            match.player1.points += 1
        elif result == "0-1":
            match.score1 = 0
            match.score2 = 1
            match.player2.points += 1
        elif result == "0.5-0.5":
            match.score1 = 0.5
            match.score2 = 0.5
            match.player1.points += 0.5
            match.player2.points += 0.5
        else:
            print("Résultat invalide. Veuillez réessayer.")
            enter_match_results(round)
            return
    save_tournaments([round.tournament])


def display_tournaments():
    tournaments = load_tournaments()
    for tournament in tournaments:
        print(f"{tournament.name} ({tournament.location})")


def display_players():
    players = load_players()
    for player in players:
        print(f"{player.last_name} {player.first_name} ({player.national_id})")


def display_tournament_details(tournament_name):
    tournaments = load_tournaments()
    for tournament in tournaments:
        if tournament.name == tournament_name:
            print(f"Tournoi : {tournament.name}")
            print(f"Date de début : {tournament.start_date}")
            print(f"Date de fin : {tournament.end_date}")
            return
    print("Tournoi non trouvé.")


def display_tournament_players(tournament_name):
    tournaments = load_tournaments()
    for tournament in tournaments:
        if tournament.name == tournament_name:
            players = sorted(tournament.players_list, key=lambda p: (p.last_name, p.first_name))
            print(f"Joueurs du tournoi {tournament.name} (ordre alphabétique) :")
            for player in players:
                print(f"{player.last_name} {player.first_name} ({player.national_id})")
            return
    print("Tournoi non trouvé.")


def display_tournament_rounds(tournament_name):
    tournaments = load_tournaments()
    for tournament in tournaments:
        if tournament.name == tournament_name:
            print(f"Rounds du tournoi {tournament.name} :")
            for round in tournament.rounds_list:
                print(f"Ronde : {round.name}")
                print(f"Date et heure de début : {round.start_time}")
                print(f"Date et heure de fin : {round.end_time}")
                for match in round.matches:
                    print(f" {match.player1.last_name} {match.player1.first_name} vs {match.player2.last_name} "
                          f"{match.player2.first_name} - Résultat : {match.score1} - {match.score2}")

            return
    print("Tournoi non trouvé.")
