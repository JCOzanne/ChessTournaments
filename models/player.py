class Player:
    def __init__(self, last_name, first_name, birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = 0

    def to_dict(self):
        """
        :return: object instance dictionary
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "points": self.points
        }

    @staticmethod
    def from_dict(data):
        """
        :param data:
        :return: object instance from dictionary
        """
        player = Player(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["national_id"]
        )
        player.points = data.get("points", 0)
        return player
