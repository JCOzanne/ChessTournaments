from utils.data_manager import load_state, save_state
from controllers.tournament_controller import (
    create_tournament,
    display_tournaments,
    display_tournament_players,
    display_tournament_details,
    display_tournament_rounds,
    resume_tournament
)
from views.report_view import display_report_menu
from views.main_view import display_main_menu
from controllers.player_controller import display_players

def main():
    state = load_state()

    if state:
        resume_tournament(state)

    while True:
        choice = display_main_menu()

        if choice == "1":
            create_tournament()

        elif choice == "2":
            while True:
                report_choice = display_report_menu()
                if report_choice == "1":
                    display_players()
                elif report_choice == "2":
                    display_tournaments()
                elif report_choice == "3":
                    tournament_name = input("Entrez le nom du tournoi: ")
                    display_tournament_details(tournament_name)
                elif report_choice == "4":
                    tournament_name = input("Entrez le nom du tournoi: ")
                    display_tournament_players(tournament_name)
                elif report_choice == "5":
                    tournament_name = input("Entrez le nom du tournoi: ")
                    display_tournament_rounds(tournament_name)
                elif report_choice == "6":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")
        elif choice == "3" and state:
            resume_tournament(state)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
