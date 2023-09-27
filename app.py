import copy
from constants import PLAYERS
from constants import TEAMS


# Function to clean player data
def clean_data(players):
    cleaned_players = copy.deepcopy(players)
    for player in cleaned_players:
        player["height"] = int(player["height"].split()[0])
        player["experience"] = player["experience"] == "YES"
        player["guardians"] = player["guardians"].split(" and ")
    return cleaned_players


# Function to balance teams
def balance_teams(players, teams):
    experienced_players = [p for p in players if p["experience"]]
    inexperienced_players = [p for p in players if not p["experience"]]

    num_players_team = len(players) // len(teams)
    num_experienced_per_team = len(experienced_players) // len(teams)
    num_inexperienced_per_team = len(inexperienced_players) // len(teams)

    for i in range(len(teams)):
        team = teams[i]
        team.extend(
            experienced_players[
                i * num_experienced_per_team : (i + 1) * num_experienced_per_team
            ]
        )
        team.extend(
            inexperienced_players[
                i * num_inexperienced_per_team : (i + 1) * num_inexperienced_per_team
            ]
        )


if __name__ == "__main__":
    # Clean the player data
    cleaned_players = clean_data(PLAYERS)

    # Initialize teams with no players
    team_panthers = []
    team_bandits = []
    team_warriors = []

    # Balance the teams
    balance_teams(cleaned_players, [team_panthers, team_bandits, team_warriors])

    # Function to display team stats
    def display_team_stats(team_name, team):
        print()
        print(f"Team: {team_name} Stats")
        print("-" * 20)
        print()
        print(f"Total players: {len(team)}")

        experienced_count = sum(1 for player in team if player["experience"])
        inexperienced_count = len(team) - experienced_count
        print(f"Total experienced: {experienced_count}")
        print(f"Total inexperienced: {inexperienced_count}")

        total_height = sum(player["height"] for player in team)
        average_height = total_height / len(team)
        print(f"Average height: {average_height:.1f}")

        player_names = ", ".join(player["name"] for player in team)
        print()
        print(f"Players on Team:\n  {player_names}")
        print()

        guardians = ", ".join(", ".join(player["guardians"]) for player in team)
        print(f"Guardians:\n  {guardians}")
        print()

    # Main menu
    while True:
        print()
        print("--------------------------")
        print("BASKETBALL TEAM STATS TOOL")
        print("--------------------------")
        print()
        print("---- MENU ----")
        print()
        print(" Here are your choices:")
        print()
        print("  A) Display Team Stats")
        print("  B) Quit")
        print()
        choice = input("Enter an option: ").strip().upper()
        print()

        if choice == "A":
            print("\nA) Panthers\nB) Bandits\nC) Warriors\n")
            team_choice = input("Enter an option: ").strip().upper()
            if team_choice == "A":
                display_team_stats("Panthers", team_panthers)
            elif team_choice == "B":
                display_team_stats("Bandits", team_bandits)
            elif team_choice == "C":
                display_team_stats("Warriors", team_warriors)
            else:
                print("Invalid team choice. Please try again.")
                print()
        elif choice == "B":
            print()
            print("Goodbye!")
            print()
            break
        else:
            print("Invalid option. Please try again.")
            print()
