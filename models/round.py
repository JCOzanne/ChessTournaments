from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name, tournament, start_time=None, end_time=None, matches=[]):
        self.name = name
        self.tournament = tournament
        self.start_time = start_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = end_time
        self.matches = matches

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.to_dict() for match in self.matches]
        }

    @staticmethod
    def from_dict(data, tournament):
        return Round(
            data["name"],
            tournament,
            data["start_time"],
            data["end_time"],
            [Match.from_dict(match_data) for match_data in data["matches"]]
        )
