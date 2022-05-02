from DreamEleven import PLAYERS
import random

class Player:
    """
    This class will be used to store the player's name, rating and title
    """

    def __init__(self, name, rating, title):
        self.name = name
        self.rating = rating
        self.title = title

# This function will be used to generate a random set of players for a particular title


def generate_title_players(team, title, number_of_players=5):
    import random 
    """
    This function will generate a dict of `number_of_players` random players from a given title
    """
    players = {}
    for i in range(number_of_players):
        player = random.choice(list(PLAYERS[title].keys()))
        while player in team.keys():
            player = random.choice(list(PLAYERS[title].keys()))
        players[player] = Player(player, PLAYERS[title][player], title)
    return players


# This function will be used to display a set of players
def display_players(players, should_display_ratings=False):
    """
    This function will display the list of players and their ratings
    """
    print(f"{'Name'.ljust(20)}{'Rating'.ljust(20) if should_display_ratings else ''}{'Title'.ljust(25)}")

    for player in players.values():
        print(
            f"{player.name.ljust(20)} {str(player.rating).ljust(20) if should_display_ratings else ''} {player.title[:-1].ljust(20)}")


def get_player_from_user(team, title, number_of_players=1):
    for i in range(number_of_players):
        # generate a set of 5 players from the list of players
        players = generate_title_players(team, title, 5)
        display_players(players=players)

        # ask the user to select a player from the list until a valid player is selected
        while True:
            player = input(
                f"Choose a {title.lower()[:-1]} #{i + 1} (by name): ")

            # check if the player is in the list of players
            if player not in PLAYERS[title]:
                print("Invalid player")
                continue

            team[player] = Player(player, PLAYERS[title][player], title)
            break


def get_player_from_computer(team, title, number_of_players=1):
    for i in range(number_of_players):
        # generate a set of 5 players from the list of players
        players = generate_title_players(team, title, 5)
        player = random.choice([k for k in players.keys()])
        team[player] = Player(player, PLAYERS[title][player], title)


# This function will be used to generate a user team of 11 players with a formation of 1-4-4-2
def generate_user_team(number_of_players=11):
    """
    This function will generate a team of 11 players i.e 1 goalkeeper 4 defenders 4 midfielders 2 attackers
    """

    user_team = {}

    # generate a goalkeeper
    get_player_from_user(user_team, 'GOALKEEPERS', 1)

    # generate 4 defenders
    get_player_from_user(user_team, 'DEFENDERS', 4)

    # generate 4 midfielders
    get_player_from_user(user_team, 'MIDFIELDERS', 4)

    # generate 2 attackers
    get_player_from_user(user_team, 'ATTACKERS', 2)

    return user_team


# This function will be used to generate a computer team of 11 players
def generate_computer_team(number_of_players=11):
    """
    This function will generate a team of 11 players
    """

    computer_team = {}

    # generate a goalkeeper
    get_player_from_computer(computer_team, 'GOALKEEPERS', 1)

    # generate 4 defenders
    get_player_from_computer(computer_team, 'DEFENDERS', 4)

    # generate 4 midfielders
    get_player_from_computer(computer_team, 'MIDFIELDERS', 4)

    # generate 2 attackers
    get_player_from_computer(computer_team, 'ATTACKERS', 2)

    return computer_team


# this function will calculates rating of a team
def calculate_team_avg_rating(team):
    """
    This function will calculate the rating of a team
    """
    rating = 0
    for player in team.values():
        rating += player.rating
    return rating / len(team)


# this function will calculate the difference between two teams average ranking
def calculate_team_difference(team1, team2):
    """
    This function will calculate the difference between two teams
    """
    return (team1) - (team2)


# main
def main():
    """
    This is the main function
    """
    # generate a user team
    user_team = generate_user_team()

    print(f"\n{'::: YOUR TEAM'.rjust(30)} :::\n")
    display_players(players=user_team, should_display_ratings=True)
    user_team_avg_rating = calculate_team_avg_rating(user_team)
    print("\n> Team Avgerage Rating: {:.2f}".format(user_team_avg_rating))

    # generate a computer team
    computer_team = generate_computer_team()

    print(f"\n{'::: COMPUTER TEAM'.rjust(30)} :::\n")
    display_players(players=computer_team, should_display_ratings=True)
    computer_team_avg_rating = calculate_team_avg_rating(computer_team)
    print("\n> Team Avgerage Rating: {:.2f}".format(computer_team_avg_rating))

    # calculate the rating difference between user team and computer team
    rating_difference = abs(
        calculate_team_difference(user_team_avg_rating, computer_team_avg_rating))

    # display the rating difference
    print("\nDIFFERENCE IN RATINGS: {:.2f}\n".format(rating_difference))


if __name__ == '__main__':
    main()