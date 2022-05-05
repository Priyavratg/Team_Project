from flask import Flask, render_template, request

app = Flask(__name__)

import random

from players import PLAYERS

def toappenddictinlist(title):
    temp = list()
    for key in PLAYERS[title]:
        temp.append(key)
    return temp

@app.route('/about')
def about():
    title = "Read about the Game"
    return render_template("about.html")

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
