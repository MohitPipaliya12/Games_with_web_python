#include <iostream>
#include <vector>
#include <iomanip>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

const int N = 5;  // Define the size of the grid (5x5)
enum Player { RED, BLUE };  // Enum to represent the players (RED and BLUE)
int score[2] = {0, 0};  // Score for both players (RED and BLUE)
char turn = 'R';  // Set the initial player to RED

// Structure to represent a move (whether it's horizontal/vertical, coordinates, and player)
struct Move {
    bool isHorizontal;
    int x, y;
    char player;
};
vector<Move> moveHistory;  // Store the history of moves

// Grids to represent the game state
vector<vector<char>> grid(N - 1, vector<char>(N - 1, ' '));  // Grid to display player moves (R/B)
vector<vector<bool>> h(N, vector<bool>(N - 1));  // Horizontal line states
vector<vector<bool>> v(N - 1, vector<bool>(N));  // Vertical line states

// ANSI color codes for coloring player marks
#define RED_COLOR "\033[31m"
#define BLUE_COLOR "\033[34m"
#define RESET_COLOR "\033[0m"

// Function to clear the screen depending on the operating system
void clearScreen() {
#ifdef _WIN32
    system("cls");  // Windows system command to clear the console
#else
    system("clear");  // Unix-based system command to clear the console
#endif
}

// Function to erase the last N lines from the console output
// This is used to clear the previous output before printing the updated grid
void eraseLastNLines(int n) {
    for (int i = 0; i < n; ++i) {
        std::cout << "\033[F\033[K";  // Move cursor up one line and clear it
    }
}

// Function to add a point to the player's score
void addScore(char t) {
    if (t == 'R') score[RED]++;  // If the move was by RED, increase RED's score
    else score[BLUE]++;  // If the move was by BLUE, increase BLUE's score
}

// Check if the coordinates are inside the grid for a horizontal or vertical line
bool isInsideGrid(bool isHorizontal, int x, int y) {
    if (isHorizontal)
        return x >= 0 && x < N && y >= 0 && y < N - 1;  // Check if horizontal line is within bounds
    else
        return x >= 0 && x < N - 1 && y >= 0 && y < N;  // Check if vertical line is within bounds
}

// Update the grid after a valid move and check if any box is completed
bool updateGrid(bool isHorizontal, int x, int y, char t) {
    bool boxCompleted = false;  // Flag to check if a box was completed

    if (isHorizontal) {  // If the move is horizontal
        if (h[x][y]) return false;  // If the horizontal line is already drawn, return false
        h[x][y] = true;  // Mark the horizontal line as drawn

        // Check if the move completes any boxes above or below the line
        if (x > 0 && h[x-1][y] && v[x-1][y] && v[x-1][y+1]) {
            grid[x-1][y] = t;  // Mark the box with the player's color
            addScore(t);  // Add score to the player
            boxCompleted = true;  // Box completed
        }
        if (x < N - 1 && h[x+1][y] && v[x][y] && v[x][y+1]) {
            grid[x][y] = t;  // Mark the box with the player's color
            addScore(t);  // Add score to the player
            boxCompleted = true;  // Box completed
        }
    } else {  // If the move is vertical
        if (v[x][y]) return false;  // If the vertical line is already drawn, return false
        v[x][y] = true;  // Mark the vertical line as drawn

        // Check if the move completes any boxes to the left or right of the line
        if (y > 0 && v[x][y-1] && h[x][y-1] && h[x+1][y-1]) {
            grid[x][y-1] = t;  // Mark the box with the player's color
            addScore(t);  // Add score to the player
            boxCompleted = true;  // Box completed
        }
        if (y < N - 1 && v[x][y+1] && h[x][y] && h[x+1][y]) {
            grid[x][y] = t;  // Mark the box with the player's color
            addScore(t);  // Add score to the player
            boxCompleted = true;  // Box completed
        }
    }

    // Store the move in the move history
    moveHistory.push_back({isHorizontal, x, y, t});
    return boxCompleted;  // Return whether a box was completed
}

// Function to print the grid with colored player marks
void printGrid() {
    int countH = 1;  // Counter for horizontal line positions
    int countV = N*(N-1) + 1;  // Counter for vertical line positions

    cout << "-----------------------------\n";
    for (int i = 0; i < N; ++i) {
        cout << "  ";
        for (int j = 0; j < N - 1; ++j) {
            cout << ". ";  // Print dots for horizontal lines
            if (h[i][j]) cout << "--- ";  // If horizontal line is drawn, display it
            else cout << setw(3) << countH << " ";  // Otherwise, display the line number
            countH++;  // Increment horizontal line counter
        }
        cout << "." << endl;

        if (i == N-1) break;  // Break after the last row
        for (int j = 0; j < N; ++j) {
            if (v[i][j]) cout << "  | ";  // Print vertical lines if drawn
            else cout << setw(3) << countV << " ";  // Display line number if vertical line isn't drawn

            if (j < N - 1) {
                // Print player marks with colors
                if (grid[i][j] == 'R') cout << RED_COLOR << 'R' << RESET_COLOR << " ";
                else if (grid[i][j] == 'B') cout << BLUE_COLOR << 'B' << RESET_COLOR << " ";
                else cout << "  ";  // If empty, print spaces
            }
            countV++;  // Increment vertical line counter
        }
        cout << endl;
    }
    cout << "-----------------------------\n";
}

// Check if the game is finished (all boxes are completed)
bool gameFinished() {
    return (score[RED] + score[BLUE] == (N - 1) * (N - 1));  // If all boxes are filled, the game is finished
}

// Function to get input from the player
bool getInput(bool &isHorizontal, int &x, int &y) {
    int input;
    cout << "If you want to back to the main menu, type 0\n";  // Option to return to main menu
    cout << "Player " << turn << "'s move (1-" << 2 * N * (N - 1) << "): ";
    cin >> input;

    if (input == 0) return false;  // Exit if the player chooses to return to the main menu

    if (input < 1 || input > 2 * N * (N - 1)) {  // If input is out of bounds, ask for input again
        eraseLastNLines(2);  // Clear the last line of output
        cout << "Invalid input! ";
        return getInput(isHorizontal, x, y);
    }

    // Determine whether the move is horizontal or vertical based on the input
    if (input <= N * (N - 1)) {
        isHorizontal = true;
        input--;
        x = input / (N - 1);  // Calculate x coordinate
        y = input % (N - 1);  // Calculate y coordinate
    } else {
        isHorizontal = false;
        input -= N * (N - 1) + 1;
        x = input / N;  // Calculate x coordinate for vertical lines
        y = input % N;  // Calculate y coordinate for vertical lines
    }

    return true;  // Return true if input is valid
}

// Save the current game state to a file
void saveGame(const string &filename) {
    ofstream out(filename);
    out << turn << ' ' << score[RED] << ' ' << score[BLUE] << '\n';
    
    // Save the horizontal line states
    for (auto &row : h) for (bool b : row) out << b << ' ';
    out << '\n';
    
    // Save the vertical line states
    for (auto &row : v) for (bool b : row) out << b << ' ';
    out << '\n';
    
    // Save the grid (player marks)
    for (auto &row : grid) for (char c : row) out << c << ' ';
    out << '\n';
    
    // Save the move history
    out << moveHistory.size() << '\n';
    for (auto &m : moveHistory)
        out << m.isHorizontal << ' ' << m.x << ' ' << m.y << ' ' << m.player << '\n';
    out.close();  // Close the file after saving
}

void loadGame(const string &filename) {
    ifstream in(filename);
    if (!in.is_open()) {
        cerr << "Error: No saved game found. Returning to main menu.\n";
        cin.ignore();
        cin.get();  // Pause to let the user read the error
        return;
    }

    char fileTurn;
    int redScore, blueScore;

    // Try to load the header (turn + scores)
    if (!(in >> fileTurn >> redScore >> blueScore)) {
        cerr << "Error: Corrupted save file header.\n";
        return;
    }

    vector<vector<bool>> tempH(N, vector<bool>(N - 1));
    vector<vector<bool>> tempV(N - 1, vector<bool>(N));
    vector<vector<char>> tempGrid(N - 1, vector<char>(N - 1));
    vector<Move> tempHistory;

    // Load horizontal lines
    for (int i = 0; i < N && in; ++i) {
        for (int j = 0; j < N - 1 && in; ++j) {
            int val;
            if (!(in >> val)) {
                cerr << "Error reading horizontal lines.\n";
                return;
            }
            tempH[i][j] = static_cast<bool>(val);
        }
    }

    // Load vertical lines
    for (int i = 0; i < N - 1 && in; ++i) {
        for (int j = 0; j < N && in; ++j) {
            int val;
            if (!(in >> val)) {
                cerr << "Error reading vertical lines.\n";
                return;
            }
            tempV[i][j] = static_cast<bool>(val);
        }
    }

    // Load grid
    for (int i = 0; i < N - 1 && in; ++i) {
        for (int j = 0; j < N - 1 && in; ++j) {
            if (!(in >> tempGrid[i][j])) {
                cerr << "Error reading grid.\n";
                return;
            }
        }
    }

    // Load move history
    int moveCount;
    if (!(in >> moveCount)) {
        cerr << "Error reading move count.\n";
        return;
    }

    for (int i = 0; i < moveCount && in; ++i) {
        Move m;
        if (!(in >> m.isHorizontal >> m.x >> m.y >> m.player)) {
            cerr << "Error reading move history.\n";
            return;
        }
        tempHistory.push_back(m);
    }

    // If everything loaded correctly, apply it to the actual game state
    turn = fileTurn;
    score[RED] = redScore;
    score[BLUE] = blueScore;
    h = tempH;
    v = tempV;
    grid = tempGrid;
    moveHistory = tempHistory;

    cout << "Game successfully loaded!\n";

    // Explicitly call printGrid here to display the loaded state
    clearScreen();
    printGrid();
    cin.ignore();
    cin.get();  // Wait for user before clearing
}

// Main function to run the game
int main() {
    bool isHorizontal;
    int x, y;
    char firstTurn = 'R';  // Set the first turn to RED
    
    while (true) {
        clearScreen();
        cout << "Welcome to Dots and Boxes Game!\n";
        cout << "1. New Game\n2. Load Game\n3. Exit\nChoose: ";
        int choice;
        cin >> choice;

        if (choice == 2) {
            ifstream test("save.txt");
            if (!test.is_open()) {
                cout << "No save file found. Please start a new game.\n";
                cin.ignore();
                cin.get();
                continue;  // Go back to the main menu
            }
            test.close();

            loadGame("save.txt");  // Load game if user chooses option 2
            // Check if game was actually loaded properly
        if (score[RED] + score[BLUE] == 0 && moveHistory.empty()) {
            cout << "Loaded game seems to be empty or invalid. Start a new game? (y/n): ";
            char retryChoice;
            cin >> retryChoice;
            if (retryChoice == 'y' || retryChoice == 'Y') {
                // Reset game state manually
                turn = 0;
                score[RED] = score[BLUE] = 0;
                moveHistory.clear();
                for (int i = 0; i < N; ++i)
                    for (int j = 0; j < N - 1; ++j)
                        h[i][j] = false;
                for (int i = 0; i < N - 1; ++i)
                    for (int j = 0; j < N; ++j)
                        v[i][j] = false;
                for (int i = 0; i < N - 1; ++i)
                    for (int j = 0; j < N - 1; ++j)
                        grid[i][j] = ' ';
            } else {
                cout << "Exiting...\n";
                return 0;
            }
        }
        } else if (choice == 3) return 0;  // Exit the game if option 3 is selected
        else if (choice == 1) {
            newGameContinue:  // Label to continue a new game
            // Reset all game variables when starting a new game
            score[RED] = 0;
            score[BLUE] = 0;
            turn = firstTurn;  // Start with RED player
            
            // Reset the grid, horizontal and vertical lines, and move history
            grid = vector<vector<char>>(N - 1, vector<char>(N - 1, ' '));
            h = vector<vector<bool>>(N, vector<bool>(N - 1, false));
            v = vector<vector<bool>>(N - 1, vector<bool>(N, false));
            moveHistory.clear();  // Clear move history
        }

        bool goMainMenu = false;  // Flag to check if the user wants to return to the main menu
        // Main game loop
        while (!gameFinished()) {
            clearScreen();
            cout << "Player R: " << setw(3) << left << score[RED] << " | Player B: " << setw(3) << left << score[BLUE] << "\n";
            printGrid();  // Display the current grid

            if (!getInput(isHorizontal, x, y)){
                goMainMenu = true;  // If user chooses to return to main menu, set the flag
                eraseLastNLines(2);  // Clear the last line of output
                cout << "Returning to main menu...\n";  // If user chooses to return to main menu, break the loop
                break;
            };  // Get input from the current player
            if (!isInsideGrid(isHorizontal, x, y)) continue;  // Validate input
            
            bool boxCompleted = updateGrid(isHorizontal, x, y, turn);  // Update grid and check if box was completed

            if (!boxCompleted) {
                turn = (turn == 'R') ? 'B' : 'R';  // Switch turn only if no box was completed
            }
        }

        // Prompt to save the game after each move
        cout << "Save game? (y/n): ";
        char save;
        cin >> save;
        if (save == 'y'){
            string filenameToSave;
            cout << "Enter filename to save (default: save.txt): "; 
            cin.ignore();  // Clear the newline character from the input buffer
            getline(cin, filenameToSave);  // Get the filename from the user
            if (filenameToSave.empty()) filenameToSave = "save.txt";  // Use default filename if none provided
            saveGame(filenameToSave);  // Save the game to the specified file
        }  // Save game if player chooses 'y'

        if (goMainMenu) continue;  // If the user chose to return to the main menu, continue the loop

        clearScreen();
        printGrid();  // Display the final grid
        cout << "Game Over!\n";
        cout << "Player R: " << score[RED] << "\n";
        cout << "Player B: " << score[BLUE] << "\n";

        // Determine the winner based on scores
        if (score[RED] > score[BLUE]) cout << "Player R wins!\n";
        else if (score[BLUE] > score[RED]) cout << "Player B wins!\n";
        else {
            cout << "It's a tie!\n";  // If scores are equal, it's a tie
            cout << "You wont to continue? (y/n): ";
            char cont;
            cin >> cont;
            if (cont == 'y') {
                // Reset game state for a new round
                score[RED] = 0;
                score[BLUE] = 0;
                // game's first turn == 'R' => turn = 'B'
                // game's first turn == 'B' => turn = 'R'
                if (firstTurn == 'R') firstTurn = 'B';  // Start with Blue player
                else firstTurn = 'R';  // Start with Red player
                
                // Reset the grid, horizontal and vertical lines, and move history
                grid = vector<vector<char>>(N - 1, vector<char>(N - 1, ' '));
                h = vector<vector<bool>>(N, vector<bool>(N - 1, false));
                v = vector<vector<bool>>(N - 1, vector<bool>(N, false));
                moveHistory.clear();  // Clear move history
                goto newGameContinue;  // Go to the new game continue label
                continue;  // Continue to the next round
            } else {
                cout << "Exiting...\n";
                return 0;  // Exit the game if user chooses not to continue
            }
        }

        
        break;  // Exit the game after a finished round
    }
    return 0;
}
// End of the game code
// This code implements a simple console-based Dots and Boxes game with features like saving/loading game state, displaying the grid with colors, and keeping track of player scores. The game is played on a 5x5 grid, and players take turns drawing lines to complete boxes. The player who completes the most boxes wins.