from posixpath import split


def get_number_of_teams():
    number_of_teams = int(input("Enter number of teams in the tournament: "))

    while number_of_teams < 2 or number_of_teams % 2 == 1:
        print("Invalid number! The tournament must contain an even number of teams and at least 2 teams.")
        number_of_teams = int(input("Enter number of teams in the tournament: "))
    
    return number_of_teams

def get_team_name(number_of_teams):
    teams_in_tournament = []
    count_of_teams = 0

    for team in range(number_of_teams):
        while True:
            team_name = input(f"Enter the name of team #{team + 1}: ")
            number_of_words = len(team_name.split(" "))

            if len(team_name) >= 2 and number_of_words <= 2:
                break   

        teams_in_tournament.append(team_name)

    return teams_in_tournament

def get_number_of_games(number_of_teams):
    while True:
        number_of_games = int(input("Enter the number of games each team has played: "))
        if number_of_games >= number_of_teams - 1:
            break
        else:
            print("Invalid number of games, each team has to play each other at least once!")

    return number_of_games


def get_number_of_wins(team_name, number_of_games):
    # team_info = []
    team_info = {}

    for i, team in enumerate(team_name):
        while True:
            wins = int(input(f"Enter how many wins {team} have: "))

            if wins < 0:
                print("The minimum number of wins is 0, try again.")
            elif wins > number_of_games:
                print("The maximum number of wins is {number_of_games}, try again.")
            else:
                # team_info.append([team, wins])
                team_info[team] = wins
                break

    return team_info
        

number_of_teams = get_number_of_teams()
team_names = get_team_name(number_of_teams)
number_of_games = get_number_of_games(number_of_teams)
team_info = get_number_of_wins(team_names, number_of_games)

sorted_teams = sorted(team_info.items(), key = lambda x: x[1])

for i in range(0, len(sorted_teams)//2):
    print(f"Away: {sorted_teams[i][0]} VS Home: {sorted_teams[-i-1][0]}")

