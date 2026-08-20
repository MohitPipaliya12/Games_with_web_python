# 🎮 Games Collection Web & Python

A collection of classic and fun games built using **Python, Flask, HTML, CSS, and JavaScript**.

The project provides a web-based Game Hub where users can select and play different games directly from their browser.

## 🌐 Live Website

🎮 **Play the games online:**  
https://games-with-web-python.onrender.com/

## 🎯 Games Included

| # | Game |
|---|---|
| 1 | 🐍 Snake Game |
| 2 | ❌ Tic Tac Toe |
| 3 | 🎮 Ultimate Tic Tac Toe |
| 4 | 🔵 Dot and Box |
| 5 | ♟️ Chess |
| 6 | 🔴 Connect Four |
| 7 | ✊ Rock Paper Scissors |
| 8 | 🧠 Memory Game |
| 9 | 🎯 Hangman |
| 10 | 💣 Minesweeper |

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Gunicorn**
- **Render**
- **Git & GitHub**

## 📁 Project Structure

```text
Games_with_web_python/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── games.py
├── dot_and_box.py
├── snake_game.py
├── TicTacToe.py
├── Tic_Tac_Toe_Grafix.py
├── uttt.py
│
├── static/
│   ├── games.css
│   ├── script.js
│   └── style.css
│
└── templates/
    ├── chess.html
    ├── connect_four.html
    ├── dot_and_box.html
    ├── hangman.html
    ├── index.html
    ├── memory_game.html
    ├── minesweeper.html
    ├── rock_paper_scissors.html
    ├── snake_game.html
    ├── tic_tac_toe.html
    └── Ultimate_Tic_Tac_Toe.html
```

## 🎮 Game Features

### 🐍 Snake Game

* 🐍 **Classic Gameplay** — Continuous snake movement, food, scoring, and game-over/collision detection.
* 🎮 **Controls & Mobile** — Keyboard, touch, and on-screen arrow controls with a responsive.
* ⚙️ **Game Options** — Restart/Play Again


### ❌ Tic Tac Toe

* ❌ **Classic Gameplay** — 3×3 two-player game with X/O turns, win/draw detection, score/result display, and invalid-move prevention.
* 🎮 **Controls & Mobile** — Mouse, touch, responsive layout, and no page scrolling.
* 🔄 **Game Controls** — Restart/Play Again and game-over display.


### 🏆 Ultimate Tic Tac Toe

* 🏆 **Ultimate Gameplay** — 9-board 3×3 layout with strategic board selection, move restrictions, turn tracking, and small/main-board win detection.
* 🎮 **Controls & Mobile** — Mouse and touch controls with responsive, mobile-friendly layout.
* 🔄 **Game Controls** — Winner/draw detection, game-over display, and New Game/Restart.


### 🔲 Dot and Boxes

* 🔲 **Classic Gameplay** — 4×4 board, 2–4 players, turn-based line drawing, box completion, scoring, and extra turns.
* 🎮 **Controls & Mobile** — Mouse and touch controls with responsive, mobile-friendly board.
* 🏆 **Game Results** — Win/tie detection, final scores, game-over screen, and Play Again/New Game.


### 🌐 Common Features

* 🌐 **Web-Based Games** — Flask server, browser gameplay, separate game pages, and clean responsive UI.
* 📱 **Cross-Device Support** — PC, mobile, and touch support with local network access.
* 🔗 **Access & Navigation** — Home page navigation, local PC hosting, and remote access through a tunnel such as Cloudflare Tunnel.




## Get Started

### 1. Clone the repository

```bash
git clone https://github.com/MohitPipaliya12/Games_with_web_python.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python games.py
```
The application will normally be available at:
```bash
http://127.0.0.1:3000
```
Open the URL in your browser and start playing.

## ☁️ Deployment

This project is deployed using:

- **GitHub** — Source code hosting
- **Render** — Web application hosting
- **Gunicorn** — Production WSGI server

### Render Configuration

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command::**

```bash
gunicorn games:app
```

🌐 **Live Website**
https://games-with-web-python.onrender.com/

## 🎮 How to Play

1. Open the **Game Hub**.
2. Select any game from the available games.
3. Play the selected game directly in your browser.
4. Use the **Back to Game Hub** button to return to the main page.
5. Select another game and continue playing.

No additional software is required to play the web-based games.


## 📌 Notes

- This project is created as a learning and game-development project.
- The web interface is built using **Flask, HTML, CSS, and JavaScript**.
- Python is used for the Flask backend and game logic.
- Static files such as CSS and JavaScript are stored in the `static/` directory.
- HTML templates are stored in the `templates/` directory.
- The `ltcode/` directory is intentionally excluded from the GitHub repository.
- The project is hosted on **Render**.
- The application may take a short time to respond if the Render service has been inactive.


## 👨‍💻 Author

**Mohit**

Computer Science Engineering Student

GitHub:  
https://github.com/MohitPipaliya12/


## ⭐ Support

If you like this project:

- ⭐ Give the repository a **Star** on GitHub.
- 🎮 Play the games and share the project with others.
- 🐛 Report bugs or issues through **GitHub Issues**.
- 💡 Suggest new games and improvements.

Your feedback and support are appreciated!

## 📜 License
This project is for learning and personal use.