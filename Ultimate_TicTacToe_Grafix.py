import tkinter as tk
from tkinter import messagebox

class UltimateTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Tic-Tac-Toe")
        self.root.configure(bg="#2E7D32")
        
        self.current_player = "O"
        self.main_board = [[None for _ in range(3)] for _ in range(3)]
        self.last_move = None
        self.center_marked = False
        
        self.label = tk.Label(self.root, text=f"{self.current_player}'s Turn", font=("Helvetica", 22, "bold"), bg="#2E7D32", fg="white")
        self.label.pack(pady=10)
        
        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#2E7D32", fg="#9FFFA6")
        self.message_label.pack(pady=5)
        
        self.create_board()
        
        # Restart Button
        self.restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 12, "bold"), bg="#FF5733", fg="white", command=self.reset_game)
        self.restart_button.pack(pady=10)
        
        # How to Play Button
        self.how_to_play_button = tk.Button(self.root, text="How to Play", font=("Helvetica", 12, "bold"), bg="#007BFF", fg="white", command=self.show_how_to_play)
        self.how_to_play_button.pack(pady=10)
    
    def create_board(self):
        self.frame = tk.Frame(self.root, bg="#2E7D32", padx=10, pady=10)
        self.frame.pack()
        
        self.buttons = [[None for _ in range(9)] for _ in range(9)]
        self.sub_frames = [[None for _ in range(3)] for _ in range(3)]
        
        for main_x in range(3):
            for main_y in range(3):
                sub_frame = tk.Frame(self.frame, relief="solid", borderwidth=2, bg="#2E7D32")
                sub_frame.grid(row=main_x, column=main_y, padx=2, pady=2)
                self.sub_frames[main_x][main_y] = sub_frame
                for sub_x in range(3):
                    for sub_y in range(3):
                        idx_x, idx_y = main_x * 3 + sub_x, main_y * 3 + sub_y
                        btn = tk.Button(sub_frame, text="", font=("Helvetica", 12, "bold"), width=4, height=2,
                                        command=lambda x=idx_x, y=idx_y: self.on_click(x, y))
                        btn.grid(row=sub_x, column=sub_y, padx=1, pady=1)
                        self.buttons[idx_x][idx_y] = btn

    def on_click(self, x, y):
        main_x, main_y = x // 3, y // 3
        sub_x, sub_y = x % 3, y % 3
        
        if self.last_move:
            target_x, target_y = self.last_move
            if self.main_board[target_x][target_y] is not None or self.center_marked:
                self.center_marked = False
            elif (main_x, main_y) != (target_x, target_y):
                self.message_label.config(text="Invalid Move: Play in the designated sub-board")
                return
        
        self.message_label.config(text="")
        
        if self.buttons[x][y]["text"] == "":
            self.buttons[x][y]["text"] = self.current_player
            self.buttons[x][y]["fg"] = "blue" if self.current_player == "O" else "red"
            
            if self.check_sub_winner(main_x, main_y):
                self.main_board[main_x][main_y] = self.current_player
                self.fill_sub_board(main_x, main_y, self.current_player)
                if self.check_winner():
                    messagebox.showinfo("Game Over", f"{self.current_player} wins the game!")
                    self.reset_game()
                    return
            
            self.current_player = "X" if self.current_player == "O" else "O"
            self.label.config(text=f"{self.current_player}'s Turn")
            self.highlight_board(sub_x, sub_y)
            self.last_move = (sub_x, sub_y)
            if self.main_board[sub_x][sub_y] is not None:
                self.center_marked = True
    
    def highlight_board(self, main_x, main_y):
        for i in range(3):
            for j in range(3):
                self.sub_frames[i][j].config(bg="#2E7D32")
        highlight_color = "red" if self.current_player == "X" else "blue"
        self.sub_frames[main_x][main_y].config(bg=highlight_color)
    
    def check_sub_winner(self, main_x, main_y):
        board = [[self.buttons[main_x * 3 + i][main_y * 3 + j]["text"] for j in range(3)] for i in range(3)]
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False
    
    def check_winner(self):
        for i in range(3):
            if self.main_board[i][0] == self.main_board[i][1] == self.main_board[i][2] is not None:
                return True
            if self.main_board[0][i] == self.main_board[1][i] == self.main_board[2][i] is not None:
                return True
        if self.main_board[0][0] == self.main_board[1][1] == self.main_board[2][2] is not None or \
           self.main_board[0][2] == self.main_board[1][1] == self.main_board[2][0] is not None:
            return True
        return False
    
    def fill_sub_board(self, main_x, main_y, player):
        fill_color = "#FF5733" if player == "X" else "#007BFF"
        for i in range(3):
            for j in range(3):
                btn = self.buttons[main_x * 3 + i][main_y * 3 + j]
                btn["text"] = player
                btn["state"] = "disabled"
                btn["bg"] = fill_color
                btn["fg"] = "white" 
        
        self.sub_frames[main_x][main_y].config(bg=fill_color)
    
    def reset_game(self):
        for i in range(9):
            for j in range(9):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"
                self.buttons[i][j]["bg"] = "SystemButtonFace"
                self.buttons[i][j]["fg"] = "black"
        for i in range(3):
            for j in range(3):
                self.sub_frames[i][j].config(bg="#2E7D32")
        self.main_board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "O"
        self.last_move = None
        self.center_marked = False
        self.label.config(text=f"{self.current_player}'s Turn")
        self.message_label.config(text="")

    def show_how_to_play(self):
        # Create a new window that is the same size as the main window
        how_to_play_window = tk.Toplevel(self.root)
        how_to_play_window.title("Rull's of Ultimate Tic-Tac-Toe")
        
        # Set the size of the new window to be the same as the main window
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        how_to_play_window.geometry(f"{window_width}x{window_height}")

        # Set the background color of the "How to Play" window to match the main window's background
        how_to_play_window.configure(bg="#2E7D32")
        
        # Add a Label with the instructions for the game
        instructions = """
                            Ultimate Tic-Tac-Toe Rules:
        
1.  The game consists of a 3x3 grid of 3x3 Tic-Tac-Toe boards.
2.  Players alternate placing their marks ('X' or 'O') in empty cells.
3.  The board you play on is determined by your previous move. 
    For example, if you place your mark in a cell in the top-left sub-board, 
    the next player must play in the top-left sub-board.
4.  If a player fills an entire sub-board with their marks (horizontal, vertical, or diagonal), 
    that sub-board is marked as complete with that player's mark.
5.  The goal is to fill an entire row, column, or diagonal in the main grid with your marks.
6.  The game ends when a player wins or all sub-boards are filled with no winner.
        """
        
        instructions_text = tk.Text(how_to_play_window, font=("Helvetica", 12), padx=20, pady=20, wrap="word", bg="#2E7D32", fg="white")
        instructions_text.insert(tk.END, instructions)
        instructions_text.config(state="disabled")  # Make text widget read-only
        instructions_text.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    game = UltimateTicTacToe(root)
    root.mainloop()
