from models.player import Player
from utils.data_manager import load_players, save_players


def add_player():
    """ create player objet and update players list
    :return:
    """
    last_name = input("Nom de famille: ")
    first_name = input("Prénom: ")
    birth_date = input("Date de naissance (JJ-MM-AAAA): ")
    national_id = input("Identifiant national d'échecs: ")
    player = Player(last_name, first_name, birth_date, national_id)
    players = load_players()
    players.append(player)
    save_players(players)
    print("Joueur ajouté avec succès!")


def display_players():
    players = load_players()
    for player in players:
        print(f"{player.last_name} {player.first_name} ({player.national_id})")
