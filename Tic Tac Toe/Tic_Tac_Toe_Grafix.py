import tkinter as tk
from tkinter import messagebox

# Function to check for a winner
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    return None

# Function to check if the game ended in a draw
def is_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

# Function to handle button clicks
def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        # Set the button color based on the player
        if current_player == "O":
            buttons[row][col].config(bg="#1D8C8C", fg="white")  # Dark teal for Player O
        else:
            buttons[row][col].config(bg="#F1FAEE", fg="black")  # Light cream for Player X
        
        winner = check_winner()

        if winner:
            winner_name = player1_name.get() if winner == "O" else player2_name.get()
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            update_score(winner)
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "X" if current_player == "O" else "O"
            # Update the label with the current player's name
            label.config(text=f"{player1_name.get() if current_player == 'O' else player2_name.get()}'s turn")

# Function to reset the game
def reset_game():
    global current_player
    if is_draw():
        current_player = "X" if current_player == "O" else "O"  # Change first player after draw
    else:
        current_player = "O"  # 'O' goes first after a win
    for row in buttons:
        for button in row:
            button["text"] = ""
            button.config(bg="#F1FAEE", fg="black")  # Reset color to default
    # Display the correct player's turn after reset
    label.config(text=f"{player1_name.get() if current_player == 'O' else player2_name.get()}'s turn")

# Function to update the score of the player
def update_score(winner):
    if winner == "O":
        player1_score.set(player1_score.get() + 1)
    else:
        player2_score.set(player2_score.get() + 1)
    # Update the score label
    score_label.config(text=f"{player1_name.get()} (O): {player1_score.get()}  |  {player2_name.get()} (X): {player2_score.get()}")

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Set background color for the window
root.config(bg="#1D3557")

# Input fields for player names
player1_name = tk.StringVar()
player2_name = tk.StringVar()

# Create a label and input field for Player 1 name
tk.Label(root, text="Enter Player 1's name (O):", font=("Helvetica", 12, "bold"), bg="#1D3557", fg="white").pack(pady=5)
player1_entry = tk.Entry(root, textvariable=player1_name, font=("Helvetica", 12), bg="#F1FAEE", fg="black", bd=2, relief="solid")
player1_entry.pack(pady=5)
player1_name.set("Player 1")  # Default value

# Create a label and input field for Player 2 name
tk.Label(root, text="Enter Player 2's name (X):", font=("Helvetica", 12, "bold"), bg="#1D3557", fg="white").pack(pady=5)
player2_entry = tk.Entry(root, textvariable=player2_name, font=("Helvetica", 12), bg="#F1FAEE", fg="black", bd=2, relief="solid")
player2_entry.pack(pady=5)
player2_name.set("Player 2")  # Default value

# Create a start game button
start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14, "bold"), command=lambda: start_game(), bg="#457B9D", fg="white", bd=0, relief="solid")
start_button.pack(pady=10)

# Initialize the current player (to be set once the game starts)
current_player = "O"  # 'O' goes first

# Create a label to display the current player
label = tk.Label(root, text=f"{player1_name.get()}'s turn", font=("Helvetica", 16, "bold"), bg="#1D3557", fg="white")
label.pack(pady=10)

# Create a score label to display both players' scores
score_label = tk.Label(root, text="Player 1 (O): 0  |  Player 2 (X): 0", font=("Helvetica", 12), bg="#1D3557", fg="white")
score_label.pack(pady=10)

# Initialize score variables for both players
player1_score = tk.IntVar()
player2_score = tk.IntVar()

# Create the game board
frame = tk.Frame(root, bg="#1D3557")
frame.pack()

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(frame, text="", font=("Helvetica", 24, "bold"), width=5, height=2, 
                           command=lambda r=i, c=j: button_click(r, c), bg="#F1FAEE", fg="black", bd=2, relief="solid")
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

# Frame for Reset and Quit buttons
button_frame = tk.Frame(root, bg="#1D3557")
button_frame.pack(pady=10)

# Reset button
reset_button = tk.Button(button_frame, text="Reset", font=("Helvetica", 14, "bold"), command=reset_game, bg="#E63946", fg="white", bd=0, relief="solid")
reset_button.pack(side="left", padx=10)

# Quit button
quit_button = tk.Button(button_frame, text="Quit", font=("Helvetica", 14, "bold"), command=root.quit, bg="#E63946", fg="white", bd=0, relief="solid")
quit_button.pack(side="left", padx=10)

# Function to start the game after entering names
def start_game():
    global current_player
    # Ensure player names are not empty
    if not player1_name.get() or not player2_name.get():
        messagebox.showerror("Error", "Both players must enter a name!")
        return

    # Hide the name entry widgets
    player1_entry.pack_forget()
    player2_entry.pack_forget()
    start_button.pack_forget()

    # Set the label for the first player
    label.config(text=f"{player1_name.get()}'s turn")

# Run the main loop
root.mainloop()
