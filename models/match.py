from models.player import Player


class Match:
    def __init__(self, player1, player2, score1=None, score2=None):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """
        :return: object instance dictionary
        """
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "score1": self.score1,
            "score2": self.score2
        }

    @staticmethod
    def from_dict(data):
        """
        :param data:
        :return: object instance from dictionary
        """
        return Match(
            Player.from_dict(data["player1"]),
            Player.from_dict(data["player2"]),
            data["score1"],
            data["score2"]
        )
