from operator import ge
from flask import Flask, render_template, request

from DreamEleven import generate_user_team, generate_computer_team, calculate_team_avg_rating, calculate_team_difference, get_player_from_user

app = Flask(__name__)

@app.route('/DreamEleven/', methods = ["GET", "POST"])
def get_team():
    Your_team = generate_user_team()
    Opponent_team = generate_computer_team()
    if request.method == "POST":
        Player_selection = request.form("Player")
        User_player = (get_player_from_user(Player_selection))
        

        return render_template("Player_Selection.html", player_name = User_player)
    return render_template("Final_Team.html", Your_team = Your_team, Opponent_team = Opponent_team)

if __name__ == '__main__':

    app.run(debug=True)