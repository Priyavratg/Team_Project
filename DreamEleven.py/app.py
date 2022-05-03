from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/team/', methods=["POST", "GET"])
def get_player():
    if request.method == "POST":
        player = request.form["player"]
        result = player
        return render_template("result.html", result2=result)
    else:
        random_players = ['a', 'b', 'c', 'd']
        return render_template("team.html", players=random_players)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        location = request.form["location"]
        result = "some result"
        return render_template("form2.html", result1=result)
    return render_template("form1.html")


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


if __name__ == "__main__":
    app.run(debug=True)