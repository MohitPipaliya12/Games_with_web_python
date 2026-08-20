# 🎮 Python Games Collection

A collection of games made with Python, Flask, HTML, CSS and JavaScript.

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


## 🛠️ Technologies

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Canvas API

## 📁 Project Structure

```text
Games_with_web&python/
├── .vscode/
├── dot_and_box.py
├── games.py
├── README.md
├── snake_game.py
├── TicTacToe.py
├── Tic_Tac_Toe_Grafix.py
├── uttt.py
│   
├───ltcode
│    ├── sudoku.cpp
│    ├── sudoku.exe
│    └── tempCodeRunnerFile.cpp
│   
├───static
│   ├── games.css
│   ├── script.js
│   └── style.css
│   
└───templates
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
    ├── Ultimate_Tic_Tac_Toe.html
```

## Get Started

### 1. check python

```bash
python --version
```
OR
```bash
py --version
```

### 2. Install Flask

```bash
pip install flask
```
OR
```bash
py -m pip install flask
```

### 3. Run the Flask Game

Open Command Prompt in the project folder.
```bash
cd .\...\Games
```
Run
```bash
python game.py
```
OR
```bash
py game.py
```
-Running on http://127.0.0.1:3000/

Run in mobile Device without Wi-Fi
```bash
cloudflared.exe tunnel --url http://localhost:3000
```
Cloudflare will give you a URL similar to:
```bash
https://powerpoint-army-phone-den.trycloudflare.com 
```
- Open that URL on your phone using mobile data.
- Your PC must have an internet connection for the tunnel to work.

## 🎮 Game URLs
Home
```bash
http://127.0.0.1:3000/
```
Snake
```bash
http://127.0.0.1:3000/play1
```
Tic Tac Toe
```bash
http://127.0.0.1:3000/play2
```
Ultimate Tic Tac Toe
```bash
http://127.0.0.1:3000/play3
```
Dot and Boxes
```bash
http://127.0.0.1:3000/play4
```

## 👨‍💻 Author
Mohit Pipaliya
GitHub: https://github.com/MohitPipaliya12

## 📜 License
This project is for learning and personal use.