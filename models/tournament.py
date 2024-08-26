from models.round import Round
from models.player import Player


class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=4, current_round=1,
                 rounds_list=[], players_list=[], description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.current_round = current_round
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description

    def to_dict(self):
        """
        :return: object instance dictionary
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": self.rounds,
            "current_round": self.current_round,
            "rounds_list": [round.to_dict() for round in self.rounds_list],
            "players_list": [player.to_dict() for player in self.players_list],
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        """
        :param data:
        :return: object instance from dictionary
        """
        tournament = Tournament(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data["rounds"],
            data["current_round"],
            [],
            [Player.from_dict(player_data) for player_data in data["players_list"]],
            data["description"]
        )
        tournament.rounds_list = [Round.from_dict(round_data, tournament) for round_data in data["rounds_list"]]
        return tournament
