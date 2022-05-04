
import random


PLAYERS = {
    'GOALKEEPERS': {
        "Jan Oblak": 91,
        "ter Stegen": 90,
        "Manuel Neuer": 90,
        "Donnarumma": 89,
        "Alisson": 89,
        "Courtois": 89,
        "Ederson": 89,
        "Keylor Navas": 88,
        "Szczesny": 87,
        "LLoris": 87,
        "Casteels": 86,
        "Handanovic": 86,
        "Schmeichel": 85,
        "Gulacsi": 85,
        "Sommer": 85,
        "Emi Martinez": 84,
        "De Gea": 84,
        "Maignan": 84,
        "Onana": 83,
        "Pickford": 83
    },

    'DEFENDERS': {
        "Van Dijk": 89,
        "Ramos": 88,
        "Marquinhos": 87,
        "Alexander Arnold": 87,
        "Robertson": 87,
        "Dias": 87,
        "Chiellini": 86,
        "Koulibaly": 86,
        "Varane": 86,
        "Alba": 86,
        "Laporte": 86,
        "Cancelo": 86,
        "Hummels": 86,
        "Skriniar": 86,
        "De Ligt": 85,
        "Bonucci": 85,
        "Hakimi": 85,
        "De Vrij": 85,
        "Walker": 85,
        "Carvajal": 85,
        "Silva": 85,
        "Digne": 84,
        "Trippier": 84,
        "Acuna": 84,
        "Ricardo Periera": 84,
        "Maguire": 84,
        "Pique": 84,
        "Jesus Navas": 84,
        "Luke Shaw": 84,
        "Ginter": 84,
        "Felipe": 84,
        "Savic": 84,
        "Guerreiro": 84,
        "Jose Gimenez": 84,
        "Alaba": 84,
        "Hernandez": 84,
        "Manolas": 83,
        "Kounde": 83,
        "Wan-Bissaka": 83,
        "Jose Gaya": 83
    },
    'MIDFIELDERS': {
        "De Bruyne": 91,
        "Kante": 90,
        "Kimmich": 89,
        "Casemiro": 89,
        "Son": 89,
        "Bruno Fernandes": 88,
        "Toni Kroos": 88,
        "Muller": 87,
        "Goretzka": 87,
        "de Jong": 87,
        "Verratti": 87,
        "Sancho": 87,
        "Pogba": 87,
        "Modric": 87,
        "Thiago": 86,
        "Fabinho": 86,
        "Coman": 86,
        "Parejo": 86,
        "Busquets": 86,
        "Rodrigo": 86,
        "Bernando Silva": 86,
        "Marcos Llorente": 86,
        "Rashford": 85,
        "Milinkovic-Savic": 85,
        "Ndidi": 85,
        "Gnabry": 85,
        "Papu Gomez": 85,
        "David Silva": 85,
        "Koke": 85,
        "Gundogan": 85,
        "Reus": 85,
        "Jorginho": 85,
        "Fekir": 84,
        "Tielemans": 84,
        "Fernando": 84,
        "Henderson": 84,
        "Luis Alebrto": 84,
        "Sane": 84,
        "Kostic": 84,
        "Sabitzer": 84
    },

    'ATTACKERS': {
        "Messi": 93,
        "Lewandowski": 92,
        "Ronaldo": 91,
        "Neymar": 91,
        "Mbappe": 91,
        "Harry Kane": 90,
        "Salah": 90,
        "Benzema": 89,
        "Mane": 89,
        "Suarez": 88,
        "Sterling": 88,
        "Haaland": 88,
        "Lukaku": 88,
        "Immobile": 87,
        "Dybala": 87,
        "Aguero": 87,
        "Di Maria": 87,
        "Vardy": 86,
        "Insigne": 86,
        "Gerard Moreno": 86,
        "Mahrez": 86,
        "Aubameyang": 85,
        "Firmino": 85,
        "Cavani": 85,
        "Oyarzabal": 85,
        "Memphis": 85,
        "Greizmann": 85,
        "Lautaro": 85,
        "Hazard": 85,
        "Aspas": 84,
        "Tadic": 84
    }
}


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
    return player

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
