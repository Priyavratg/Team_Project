from flask import Flask, render_template, request

app = Flask(__name__)

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
    print(get_player_from_user(user_team, 'GOALKEEPERS', 1))

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


@app.route('/team/', methods=["POST", "GET"])
def get_player():
    if request.method == "POST":
        player = request.form["player"]
        result = player
        return render_template("result.html", result2=result)
    else:
        random_players = ['a', 'b', 'c', 'd']
        return render_template("team.html", players=random_players)


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        location = request.form["location"]
        result = "some new result"
        return render_template("result.html", result2=result)
    return render_template("form2.html")


@app.route('/start')
def start_page():
    return render_template('start.html')


@app.route('/upload')
def upload_file():
    return 'hi'


def toappenddictinlist(title):
    temp = list()
    for key in PLAYERS[title]:
        temp.append(key)
    return temp


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        golkeeper = request.form.get('golkeeper')
        defender1 = request.form.get('defender1')
        defender2 = request.form.get('defender2')
        defender3 = request.form.get('defender3')
        defender4 = request.form.get('defender4')

        modifier1 = request.form.get('modifier1')
        modifier2 = request.form.get('modifier2')
        modifier3 = request.form.get('modifier3')
        modifier4 = request.form.get('modifier4')

        forward1 = request.form.get('forward1')
        forward2 = request.form.get('forward2')

        result = 0
        if golkeeper in PLAYERS['GOALKEEPERS']:
            result = result + PLAYERS['GOALKEEPERS'][golkeeper]

        if defender1 in PLAYERS['DEFENDERS']:
            result = result + PLAYERS['DEFENDERS'][defender1]

        if defender2 in PLAYERS['DEFENDERS']:
            result = result + PLAYERS['DEFENDERS'][defender2]

        if defender3 in PLAYERS['DEFENDERS']:
            result = result + PLAYERS['DEFENDERS'][defender3]

        if defender4 in PLAYERS['DEFENDERS']:
            result = result + PLAYERS['DEFENDERS'][defender4]

        if modifier1 in PLAYERS['MIDFIELDERS']:
            result = result + PLAYERS['MIDFIELDERS'][modifier1]

        if modifier2 in PLAYERS['MIDFIELDERS']:
            result = result + PLAYERS['MIDFIELDERS'][modifier2]

        if modifier3 in PLAYERS['MIDFIELDERS']:
            result = result + PLAYERS['MIDFIELDERS'][modifier3]

        if modifier4 in PLAYERS['MIDFIELDERS']:
            result = result + PLAYERS['MIDFIELDERS'][modifier4]

        if forward1 in PLAYERS['ATTACKERS']:
            result = result + PLAYERS['ATTACKERS'][forward1]

        if forward2 in PLAYERS['ATTACKERS']:
            result = result + PLAYERS['ATTACKERS'][forward2]

        result = result / 11

        # Now start getting computer team
        extra_list = list()

        goal_keys = list(PLAYERS['GOALKEEPERS'].keys())
        check = 1
        while check == 1:
            ran = random.randint(0, 19)
            temporar = goal_keys[ran]
            if str(temporar) != str(golkeeper):
                check = 0

        computergolkeeper = temporar
        extra_list.append(computergolkeeper)

        defend_keys = list(PLAYERS['DEFENDERS'].keys())
        check = 1
        while check == 1:
            temporar = defend_keys[random.randint(0, 10)]
            if str(temporar) != str(defender1):
                if str(temporar) not in extra_list:
                    check = 0

        computerdefender1 = temporar
        extra_list.append(computerdefender1)

        check = 1
        while check == 1:
            temporar = defend_keys[random.randint(0, 10)]
            if str(temporar) != str(defender2):
                if str(temporar) not in extra_list:
                    check = 0

        computerdefender2 = temporar
        extra_list.append(computerdefender2)

        check = 1
        while check == 1:
            temporar = defend_keys[random.randint(0, 10)]
            if str(temporar) != str(defender3):
                if str(temporar) not in extra_list:
                    check = 0

        computerdefender3 = temporar
        extra_list.append(computerdefender3)

        check = 1
        while check == 1:
            temporar = defend_keys[random.randint(0, 10)]
            if str(temporar) != str(defender4):
                if str(temporar) not in extra_list:
                    check = 0

        computerdefender4 = temporar
        extra_list.append(computerdefender4)

        modify_keys = list(PLAYERS['MIDFIELDERS'].keys())

        check = 1
        while check == 1:
            temporar = modify_keys[random.randint(0, 10)]
            if str(temporar) != str(modifier1):
                if str(temporar) not in extra_list:
                    check = 0

        computermodifier1 = temporar
        extra_list.append(computermodifier1)

        check = 1
        while check == 1:
            temporar = modify_keys[random.randint(0, 10)]
            if str(temporar) != str(modifier2):
                if str(temporar) not in extra_list:
                    check = 0

        computermodifier2 = temporar
        extra_list.append(computermodifier2)

        check = 1
        while check == 1:
            temporar = modify_keys[random.randint(0, 10)]
            if str(temporar) != str(modifier3):
                if str(temporar) not in extra_list:
                    check = 0

        computermodifier3 = temporar
        extra_list.append(computermodifier3)

        check = 1
        while check == 1:
            temporar = modify_keys[random.randint(0, 10)]
            if str(temporar) != str(modifier4):
                if str(temporar) not in extra_list:
                    check = 0

        computermodifier4 = temporar
        extra_list.append(computermodifier4)

        attack_keys = list(PLAYERS['ATTACKERS'].keys())

        check = 1
        while check == 1:
            temporar = attack_keys[random.randint(0, 10)]
            if str(temporar) != str(forward1):
                if str(temporar) not in extra_list:
                    check = 0

        computerforward1 = temporar
        extra_list.append(computerforward1)

        check = 1
        while check == 1:
            temporar = attack_keys[random.randint(0, 10)]
            if str(temporar) != str(forward2):
                if str(temporar) not in extra_list:
                    check = 0

        computerforward2 = temporar
        extra_list.append(computerforward2)



        result2 = 0
        if computergolkeeper in PLAYERS['GOALKEEPERS']:
            result2 = result2 + PLAYERS['GOALKEEPERS'][computergolkeeper]

        if computerdefender1 in PLAYERS['DEFENDERS']:
            result2 = result2 + PLAYERS['DEFENDERS'][computerdefender1]

        if computerdefender2 in PLAYERS['DEFENDERS']:
            result2 = result2 + PLAYERS['DEFENDERS'][computerdefender2]

        if computerdefender3 in PLAYERS['DEFENDERS']:
            result2 = result2 + PLAYERS['DEFENDERS'][computerdefender3]

        if computerdefender4 in PLAYERS['DEFENDERS']:
            result2 = result2 + PLAYERS['DEFENDERS'][computerdefender4]

        if computermodifier1 in PLAYERS['MIDFIELDERS']:
            result2 = result2 + PLAYERS['MIDFIELDERS'][computermodifier1]

        if computermodifier2 in PLAYERS['MIDFIELDERS']:
            result2 = result2 + PLAYERS['MIDFIELDERS'][computermodifier2]

        if computermodifier3 in PLAYERS['MIDFIELDERS']:
            result2 = result2 + PLAYERS['MIDFIELDERS'][computermodifier3]

        if computermodifier4 in PLAYERS['MIDFIELDERS']:
            result2 = result2 + PLAYERS['MIDFIELDERS'][computermodifier4]

        if computerforward1 in PLAYERS['ATTACKERS']:
            result2 = result2 + PLAYERS['ATTACKERS'][computerforward1]

        if computerforward2 in PLAYERS['ATTACKERS']:
            result2 = result2 + PLAYERS['ATTACKERS'][computerforward2]

        result2 = result2 / 11
        print(result2)

        difference = result - result2

        return render_template("form2.html", result1=result,
                               golkeeper=golkeeper,
                               defender1=defender1,
                               defender2=defender2,
                               defender3=defender3,
                               defender4=defender4,

                               midfielder1=modifier1,
                               moidfielder2=modifier2,
                               midfielder3=modifier3,
                               midfielder4=modifier4,

                               forward1=forward1,
                               forward2=forward2,
                               result=result,
                               result2=result2,
                               difference=difference,

                               computergolkeeper=computergolkeeper,

                               computerdefender1=computerdefender1,
                               computerdefender2=computerdefender2,
                               computerdefender3=computerdefender3,
                               computerdefender4=computerdefender4,

                               computermodifier1=computermodifier1,
                               computermodifier2=computermodifier2,
                               computermodifier3=computermodifier3,
                               computermodifier4=computermodifier4,

                               computerforward1=computerforward1,
                               computerforward2=computerforward2

                               )

    golkeeper_temp = toappenddictinlist('GOALKEEPERS')
    choose_five = list()
    count = 0
    check = 0
    while check == 0:
        generate = golkeeper_temp[random.randint(0, 19)]
        if count == 4:
            check = 1
        if generate not in choose_five:
            choose_five.append(generate)
            count = count + 1

    defender_temp = toappenddictinlist('DEFENDERS')
    count = 0
    check = 0
    choose_twenty = list()
    while check == 0:
        generate = defender_temp[random.randint(0, 19)]
        if count == 20:
            check = 1
        if generate not in choose_twenty:
            choose_twenty.append(generate)
            count = count + 1

    # DEFENDERS
    defender_temp1 = [choose_twenty[0], choose_twenty[1], choose_twenty[2], choose_twenty[3], choose_twenty[4]]
    defender_temp2 = [choose_twenty[5], choose_twenty[6], choose_twenty[7], choose_twenty[8], choose_twenty[9]]
    defender_temp3 = [choose_twenty[10], choose_twenty[11], choose_twenty[12], choose_twenty[13], choose_twenty[14]]
    defender_temp4 = [choose_twenty[15], choose_twenty[16], choose_twenty[17], choose_twenty[18], choose_twenty[19]]

    midfielder_temp = toappenddictinlist('MIDFIELDERS')
    count = 0
    check = 0
    choose_twenty_midfielder = list()
    while check == 0:
        generate = midfielder_temp[random.randint(0, 19)]
        if count == 20:
            check = 1
        if generate not in choose_twenty:
            choose_twenty_midfielder.append(generate)
            count = count + 1

        # Modifier
    midfielder_temp1 = [choose_twenty_midfielder[0], choose_twenty_midfielder[1], choose_twenty_midfielder[2],
                        choose_twenty_midfielder[3], choose_twenty_midfielder[4]]
    midfielder_temp2 = [choose_twenty_midfielder[5], choose_twenty_midfielder[6], choose_twenty_midfielder[7],
                        choose_twenty_midfielder[8], choose_twenty_midfielder[9]]
    midfielder_temp3 = [choose_twenty_midfielder[10], choose_twenty_midfielder[11], choose_twenty_midfielder[12],
                        choose_twenty_midfielder[13], choose_twenty_midfielder[14]]
    midfielder_temp4 = [choose_twenty_midfielder[15], choose_twenty_midfielder[16], choose_twenty_midfielder[17],
                        choose_twenty_midfielder[18], choose_twenty_midfielder[19]]

    attacker_temp = toappenddictinlist('ATTACKERS')
    count = 0
    check = 0
    choose_twenty_attacker = list()
    while check == 0:
        generate = attacker_temp[random.randint(0, 19)]
        if count == 10:
            check = 1
        if generate not in choose_twenty:
            choose_twenty_attacker.append(generate)
            count = count + 1

        # Modifier
    attacker_temp1 = [choose_twenty_attacker[0], choose_twenty_attacker[1], choose_twenty_attacker[2],
                      choose_twenty_attacker[3], choose_twenty_attacker[4]]
    attacker_temp2 = [choose_twenty_attacker[5], choose_twenty_attacker[6], choose_twenty_attacker[7],
                      choose_twenty_attacker[8], choose_twenty_attacker[9]]

    return render_template("form1.html", choose_five=choose_five,
                           defender_temp1=defender_temp1,
                           defender_temp2=defender_temp2,
                           defender_temp3=defender_temp3,
                           defender_temp4=defender_temp4,
                           midfielder_temp1=midfielder_temp1,
                           midfielder_temp2=midfielder_temp2,
                           midfielder_temp3=midfielder_temp3,
                           midfielder_temp4=midfielder_temp4,
                           attacker_temp1=attacker_temp1,
                           attacker_temp2=attacker_temp2
                           )


if __name__ == "__main__":
    app.run(debug=True)
