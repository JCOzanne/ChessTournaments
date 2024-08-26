import json
import os
from models.player import Player
from models.tournament import Tournament


def load_players():
    """
    :return: a list of instances of Player
    """
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/players.json"):
        with open("data/players.json", "w") as file:
            json.dump([], file)
    with open("data/players.json", "r") as file:
        data = json.load(file)
        return [Player.from_dict(player_data) for player_data in data]


def save_players(players):
    """
    :param players:
    :return: a json file of Player Objects
    """
    if not os.path.exists("data"):
        os.makedirs("data")
    with open("data/players.json", "w") as file:
        json.dump([player.to_dict() for player in players], file, indent=4)


def load_tournaments():
    """
    :return: a list of instances of tournaments
    """
    if not os.path.exists("data/tournaments"):
        os.makedirs("data/tournaments")
    tournaments = []
    tournament_files = os.listdir("data/tournaments")
    for file_name in tournament_files:
        if file_name.endswith(".json"):
            with open(f"data/tournaments/{file_name}", "r") as file:
                data = json.load(file)
                tournament = Tournament.from_dict(data)
                tournaments.append(tournament)
    return tournaments


def save_tournaments(tournaments):
    """
    :param tournaments:
    :return: a json file of Tournaments Objects
    """
    if not os.path.exists("data/tournaments"):
        os.makedirs("data/tournaments")
    for tournament in tournaments:
        file_name = f"data/tournaments/{tournament.name}.json"
        with open(file_name, "w") as file:
            json.dump(tournament.to_dict(), file, indent=4)
