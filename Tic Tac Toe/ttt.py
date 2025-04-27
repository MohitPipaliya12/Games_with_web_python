from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/play")
def play_game():
    return render_template("tic_tac_toe.html")  # <-- render web Tic Tac Toe

if __name__ == "__main__":
    app.run(debug=True)
