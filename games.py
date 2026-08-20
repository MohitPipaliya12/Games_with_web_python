from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play1")
def play_snake():
    return render_template("snake_game.html")

@app.route("/play2")
def play_tic_tac_toe():
    return render_template("tic_tac_toe.html")

@app.route("/play3")
def play_ultimate_tic_tac_toe():
    return render_template("Ultimate_Tic_Tac_Toe.html")

@app.route("/play4")
def play_dot_and_boxes():
    return render_template("dot_and_box.html")

# Upcoming games
@app.route("/play5")
def play_chess():
    return render_template("chess.html")


@app.route("/play6")
def play_connect_four():
    return render_template("connect_four.html")


@app.route("/play7")
def play_rock_paper_scissors():
    return render_template("rock_paper_scissors.html")


@app.route("/play8")
def play_memory_game():
    return render_template("memory_game.html")


@app.route("/play9")
def play_hangman():
    return render_template("hangman.html")


@app.route("/play10")
def play_minesweeper():
    return render_template("minesweeper.html")

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=3000,
        debug=True,
        use_reloader=False
    )
    
# The use_reloader=False argument is added to prevent the app from running twice in debug mode.
# This is a common issue with Flask's reloader, which can cause the app to start twice.