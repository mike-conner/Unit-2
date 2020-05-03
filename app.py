"""
---------------------------------
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
Mike Conner
05/01/2020
---------------------------------
"""

import constants
import copy


def clean_data(PLAYERS, TEAMS):
    players = copy.deepcopy(PLAYERS)
    teams = copy.deepcopy(TEAMS)

    for player in players:
        for key, value in player.items():
            # convert player heights from strings to ints
            # (e.g. '42 inches' -> 42)
            if key == 'height':
                temp_array = value.split()
                player[key] = int(temp_array[0])

            # convert player experience from strings to booleans
            # (e.g. 'YES' -> True)
            if key == 'experience':
                if value == 'YES':
                    player[key] = True
                else:
                    player[key] = False

            # remove ' and ' when there are more than one guardian
            # (e.g. Charles Gill and Sylvia Gill -> Charles Gill, Sylvia Gill)
            if key == 'guardians':
                player[key] = value.split(' and ')

    return players, teams


def balance_teams(players, teams):
    number_of_teams = len(teams)
    number_of_players = len(players)

    team_counter = 0
    player_counter = 0

    # add a key to the nested dictionaries to store the assigned team
    for item in players:
        item.update({'team': ''})

    # assign a team to each experienced player
    players, team_counter = experience_sort(player_counter,number_of_players,
                                            players,teams,team_counter,
                                            number_of_teams, True)
    player_counter = 0
    # assign a team to each inexperienced player
    players, team_counter = experience_sort(player_counter, number_of_players,
                                            players, teams,team_counter,
                                            number_of_teams, False)

    return players


# experience_sort assigns a team to each player
def experience_sort(player_counter, number_of_players, players, teams,
                    team_counter, number_of_teams, is_experienced):
    while player_counter < number_of_players:
        for player in players:
            for key, value in player.items():
                # conditional test to see if the play has experience or not
                if key == 'experience' and value == is_experienced:
                    # assign next team to player's team key
                    players[player_counter]['team'] = teams[team_counter]
                    # after assigning team, go to next team in list
                    if team_counter < (number_of_teams - 1):
                        team_counter += 1
                    # or if at last team, go to first team in list
                    else:
                        team_counter = 0
            # increment counter until all players in list have a team
            player_counter += 1

    # return the player list with a teams now assigned to their key
    # return the team_counter variable to keep track of last team assigned
    # so if the function is called again it picks up where it left off
    return players, team_counter


def show_welcome_message():
    print('''
=============================================
         BASKETBALL TEAM STATS TOOL
=============================================
''')


def get_user_choice():
    print('''
Please select from the following:
1)  Display The Panther's Stats
2)  Display The Bandit's Stats
3)  Display The Warrior's Stats
4)  Quit
''')

    while True:
        try:
            user_choice = int(input('Please enter your choice ->  '))
            if user_choice not in range(1, 5):
                raise ValueError
        except ValueError:
            print("\nThat is not a valid option. Please try again.\n")
        else:
            break

    return user_choice


def get_stats(team, players):
    player_count = 0
    experience_count = 0
    inexperience_count = 0

    total_height = 0

    roster = []
    guardians = []
    flat_guardian_list = []

    for player in players:
        for key, value in player.items():
            if value == team:
                roster.append(player['name'])
                guardians.append(player['guardians'])
                player_count += 1
                if player['experience'] == True:
                    experience_count += 1
                else:
                    inexperience_count += 1
                total_height += player['height']

    for outer in guardians:
        for inner in outer:
            flat_guardian_list.append(inner)

    # take the roster and guardian list and format them for readability
    pretty_print_roster = ', '.join(roster)
    pretty_print_guardians = ', '.join(flat_guardian_list)

    # fuction call to print the stats obtained above in this function
    display_stats(team, player_count, experience_count, inexperience_count,
                  round((total_height / player_count), 2), pretty_print_roster,
                  pretty_print_guardians)


def display_stats(team, player_count, experience_count, inexperience_count,
                  average_height, roster, guardians):
    print('\n')
    print('*' * 79)
    print('''
--------------------
Team: {} Stats
--------------------

Total Players:               {}
Total Experienced Players:   {}
Total Inexperienced Players: {}
Average Height:              {}


Players on Team:
{}


Guardians:
{}

'''.format(team, player_count, experience_count, inexperience_count,
           average_height, roster, guardians)
)
    print('*' * 79)


def begin_application():
    # make copies and clean up data in constants.py
    players, teams = clean_data(constants.PLAYERS, constants.TEAMS)

    # sort the data and assign teams to each player
    assigned_players = balance_teams(players, teams)

    show_welcome_message()

    # loop getting user's choice of which stats to view or to quit the app
    while True:
        user_choice = get_user_choice()

        if user_choice == 1:
            get_stats('Panthers', assigned_players)
        elif user_choice == 2:
            get_stats('Bandits', assigned_players)
        elif user_choice == 3:
            get_stats('Warriors', assigned_players)
        else:
            # quit program
            break


if __name__ == '__main__':
    begin_application()
