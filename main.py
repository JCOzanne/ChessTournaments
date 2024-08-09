from datetime import datetime


class Player:

    def __init__(
            self,
            first_name: str,
            last_name: str,
            birthday: str,
            national_chess_id: str,
            rating=int
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.national_chess_id = national_chess_id
        self.rating = rating
        self.score = 0.0
        self.opponents = []

    def __str__(self):
        """
        :return: readable version of a player
        """
        return (f"{self.first_name} {self.last_name} "
                f"(Anniversaire : {self.birthday}, Identifiant National d'Echecs: {self.national_chess_id}, Evaluation: {self.rating}, Score: {self.score})")

    def add_opponent(self, opponent_id: str):
        """
        :param opponent_id:
        :return: list of opponent
        """

        self.opponents.append(opponent_id)

    def update_score(self, points: float):
        """
        :param points:
        :return: score updated after a match
        """

        self.score += points

    def to_dict(self):
        """
        :return: a dictionary containing a player's information
        """

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "national_chess_id": self.national_chess_id,
            "rating": self.rating,
            "score": self.score,
            "opponent": self.opponents
        }


# player1 = Player("Firoujza", "Alireza", "18-06-2003", "AB12345", 2760)
# player2 = Player("Vachier_Lagrave", "Maxime", "21-10-1990", "CD45698", 2732)
# print(f"Adversaires de {player1.first_name} {player1.last_name} ({player1.national_chess_id}): {player1.opponents}")

class Match:

    def __init__(self, player_1: Player, player_2: Player):
        self.match = ([player_1, 0], [player_2, 0])

    def __str__(self):
        """
        :return: readable version of a match
        """
        player1, score1 = self.match[0]
        player2, score2 = self.match[1]
        return f"{player1} : {score1}\n{player2} : {score2}"

    def match_set_result(self, result: str):
        """
        :param result: result of a chess match
        :return:score of the player
        """
        if result == "1-0":
            self.match[0][1] = 1
            self.match[1][1] = 0
        elif result == "0-1":
            self.match[0][1] = 0
            self.match[1][1] = 1
        elif result == "0-0":
            self.match[0][1] = 0.5
            self.match[1][1] = 0.5

    def match_get_result(self):
        """
        :return: the result of a match - player1 (id, rating, score) : point won/lost
                                       - player2 (id, rating, score) : point won/lost
        """
        return self.match


# player1 = Player("Firoujza", "Alireza", "18-06-2003", "AB12345", 2760)
# player2 = Player("Vachier_Lagrave", "Maxime", "21-10-1990", "CD45698", 2732)
# match = Match(player1, player2)
# match.match_set_result("1-0")
# print(match)

class Round:
    def __init__(self, round_name):
        self.round_name = round_name
        self.start_date = datetime.now()
        self.end_date = None
        self.matches = []

    def add_match(self, match: Match):
        """
        :return: add a match to the list matches
        """
        self.matches.append(match)

    def end_round(self):
        """

        :return: end date of the round
        """
        self.end_date = datetime.now()

    def round_get_result(self):
        """

        :return: the result of the round in the form (identifier1, identifier2): (score 1, score 2)
        """
        results = {}
        for match in self.matches:
            player1_score1, player2_score2 = match.match_get_result()
            results[(player1_score1[0].national_chess_id, player2_score2[0].national_chess_id)] \
                = (player1_score1[1], player2_score2[1])
        return results


# player1 = Player("Firoujza", "Alireza", "18-06-2003", "AB12345", 2760)
# player2 = Player("Vachier_Lagrave", "Maxime", "21-10-1990", "CD45698", 2732)
# player3 = Player("Bacrot", "Etienne", "22-01*1983", "EF98651", 2683 )
# player4 = Player("Fressinet", "Laurent", "30-11-1981", "GH56782", 2637)
#
# match1 = Match(player1, player2)
# match2 = Match(player3, player4)
# match1.match_set_result("1-0")
# match2.match_set_result("0-0")
#
# round1 = Round(round_name="Round 1")
# round1.add_match(match1)
# round1.add_match(match2)
#
# round_results = round1.round_get_result()
# print(round_results)

class Tournament:

    def __init__(
            self,
            tournament_name: str,
            location: str,
            start_date: str,
            end_date: str,
            players: list,
            num_rounds=4,
            description=""
    ):
        self.tournament_name = tournament_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.num_rounds = num_rounds
        self.description = description
        self.current_round = 0
        self.rounds = []
        self.previous_pairs = set()

    def generate_pairs(self):
        """
        :return: sorted pairs of players avoiding creating pairs that existed
        """
        sorted_players = sorted(self.players, key=lambda play: (-play.score, play.national_chess_id))
        pairs = []
        i = 0

        while i < len(sorted_players) - 1:
            player1 = sorted_players[i]
            player2 = sorted_players[i + 1]

            j = i + 1
            while j < len(sorted_players) and (
            player1.national_chess_id, sorted_players[j].national_chess_id) in self.previous_pairs:
                j += 1

            if j < len(sorted_players):
                player2 = sorted_players[j]
                sorted_players[i + 1], sorted_players[j] = sorted_players[j], sorted_players[i + 1]

            pairs.append((player1, player2))
            self.previous_pairs.add((player1.national_chess_id, player2.national_chess_id))
            i += 2

        return pairs

    def get_players_sorted_by_name(self):
        """
        :return: Sorted list of players
        """
        return sorted(self.players, key=lambda play: (play.last_name, play.first_name))

    def display_players(self):
        """

        :return: List of tournament players in alphabetical order.
        """
        sorted_players = self.get_players_sorted_by_name()
        print("\nListe des joueurs par ordre alphabétique:")
        for player in sorted_players:
            print(player)

    def display_rounds_and_matches(self):
        """

        :return: list of all tournament rounds and all round matches.
        """
        print("\nListe des tours du tournoi et des matchs du tour:")
        for rnd in self.rounds:
            print(f"\n{rnd.round_name} - Début: {rnd.start_date}, Fin: {rnd.end_date}")
            for match in rnd.matches:
                print(match)



    def add_round(self):
        """

        :return:
        """
        if self.current_round >= self.num_rounds:
            print("Le nombre maximum de tours a été atteint.")
            return

        self.current_round += 1
        round_name = f"Round {self.current_round}"
        new_round = Round(round_name=round_name)
        new_round.matches = []
        for p1, p2 in self.generate_pairs():
            new_round.matches.append(Match(p1, p2))
        self.rounds.append(new_round)
        # print(f"{round_name} a été ajouté.")

    def get_current_round(self):
        return self.current_round

    def is_tournament_complete(self):
        return self.current_round >= self.num_rounds

# simulation d'un tournois avec player1 gagne tous ses matchs, player2 gagne 2 matchs, player3 gagne 1 match
# et player4 gagne 0 match.
# le programme retourne :
#- le nom du tournois("Tournoi de Paris") et la date du tournoi (le 09/08/2024),
#- la liste de tous les joueurs par ordre alphabétique,
#- liste de tous les tours du tournoi et de tous les matchs du tour
#- la description : "Ce tournoi est organisé pour sélectionner les meilleurs joueurs pour la finale nationale."

# 1- Initialisation des joueurs

player1 = Player("Firoujza", "Alireza", "18-06-2003", "AB12345", 2760)
player2 = Player("Vachier_Lagrave", "Maxime", "21-10-1990", "CD45698", 2732)
player3 = Player("Bacrot", "Etienne", "22-01-1983", "EF98651", 2683 )
player4 = Player("Fressinet", "Laurent", "30-11-1981", "GH56782", 2637)

# 2- Création du tournois

tournament = Tournament(
    tournament_name="Tournoi de Paris",
    location="Paris",
    start_date="09-08-2024",
    end_date="09-08-2024",
    players=[player1, player2, player3, player4],
    description="Ce tournoi est organisé pour sélectionner les meilleurs joueurs pour la finale nationale."
)

# 3- Simulation des Rounds et des Matchs avec les résultats

tournament.add_round()
tournament.rounds[0].matches[0].match_set_result("1-0")
tournament.rounds[0].matches[1].match_set_result("1-0")


player1.update_score(1)
player2.update_score(0)
player3.update_score(1)
player4.update_score(0)


tournament.add_round()
tournament.rounds[1].matches[0].match_set_result("1-0")
tournament.rounds[1].matches[1].match_set_result("1-0")


player1.update_score(1)
player2.update_score(1)
player3.update_score(0)
player4.update_score(0)


tournament.add_round()
tournament.rounds[2].matches[0].match_set_result("1-0")
tournament.rounds[2].matches[1].match_set_result("0-1")

player1.update_score(1)
player2.update_score(1)
player3.update_score(0)
player4.update_score(0)


# 4- Affichage des résultats

print(f"Nom du Tournoi: {tournament.tournament_name}")
print(f"Date du Tournoi: {tournament.start_date}")
print(f"Description: {tournament.description}")


tournament.display_players()

tournament.display_rounds_and_matches()













