#include <iostream>
#include <vector>
#include <iomanip> // for std::setw

using namespace std;

const int N = 5; // Grid Size (N x N)
enum Player { RED, BLUE };
int score[2] = {0, 0};
char turn = 'R';  // 'R' or 'B'

vector<vector<char>> grid(N - 1, vector<char>(N - 1, ' '));
vector<vector<bool>> h(N, vector<bool>(N - 1));
vector<vector<bool>> v(N - 1, vector<bool>(N));

// Cross-platform screen clear
void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

bool isInsideGrid(bool isHorizontal, int x, int y) {
    if (isHorizontal)   // Horizontal
        return x >= 0 && x < N && y >= 0 && y < N - 1;
    else                // Vertical
        return x >= 0 && x < N - 1 && y >= 0 && y < N;
}

void addScore(char turn) {
    if (turn == 'R') score[RED]++;
    else score[BLUE]++;
}

bool updateGrid(bool isHorizontal, int x, int y, char turn) {
    bool boxCompleted = false;

    if (isHorizontal) {          // horizontal
        if (h[x][y]) {
            cout << "Line already filled!\n";
            return false;
        }
        h[x][y] = true;

        if (x > 0 && h[x-1][y] && v[x-1][y] && v[x-1][y+1]) {
            grid[x-1][y] = turn;
            addScore(turn);
            boxCompleted = true;
        }
        if (x < N - 1 && h[x+1][y] && v[x][y] && v[x][y+1]) {
            grid[x][y] = turn;
            addScore(turn);
            boxCompleted = true;
        }
    } else {            // vertical
        if (v[x][y]) {
            cout << "Line already filled!" << endl;
            return false;
        }
        v[x][y] = true;

        if (y > 0 && v[x][y-1] && h[x][y-1] && h[x+1][y-1]) {
            grid[x][y-1] = turn;
            addScore(turn);
            boxCompleted = true;
        }
        if ( y < N - 1 &&v[x][y+1] && h[x][y] && h[x+1][y]) {
            grid[x][y] = turn;
            addScore(turn);
            boxCompleted = true;
        }
    }
    return boxCompleted;
}

void printGrid() {
    cout << N << " x " << N << " Grid:\n";
    cout << "===========================\n";

    // cout << "     ";
    // for (int j = 0; j < N; ++j) cout << j+1 << "   ";
    // cout << endl;

    int countH = 1;
    int countV = N*(N-1) + 1;
    for (int i = 0; i < N; ++i) {
        // cout << "  " << i+1 << " ";
        cout << "  ";
        for (int j = 0; j < N-1; ++j) {
            cout << ". ";
            if(h[i][j])
                cout << "--- ";
            else
                cout << setw(3) << countH << " ";
            countH++;
        }
        cout << "." << endl;

        if (i == N-1) break;
        // cout << "    ";
        for (int j = 0; j < N; ++j) {
            if(v[i][j])
                cout << "  | ";
            else
                cout << setw(3) << countV << " ";
            if (j < N-1) cout << grid[i][j] << " ";
            countV++;
        }
        cout << endl;
    }
    cout << "===========================" << endl;
}
/*
. - . - . - . - .
|   |   |   |   |
. - . - . - . - .
|   |   |   |   |
. - . - . - . - .
|   |   |   |   |
. - . - . - . - .
|   |   |   |   |
. - . - . - . - .

*/

bool gameFinished() {
    return (score[RED] + score[BLUE] == (N - 1) * (N - 1));
}

void getInput(bool &isHorizontal, int &x, int &y) {
    int input;
    // cout << "Enter 1 for Horizontal, 0 for Vertical line, then row and column (1-based): \n";
    cout << "Player " << turn << "'s turn (1-" << 2 * N * (N - 1) << "): ";
    cin >> input;

    if (input < 1 || input > 2 * N * (N - 1)) {
        cout << "Invalid input! Try again.\n";
        return getInput(isHorizontal, x, y); // Or loop back in main
    }   

    if (input <= N * (N - 1)) {
        isHorizontal = true;
        input--;  // 0-based index
        x = input / (N - 1);
        y = input % (N - 1);
    } else {
        isHorizontal = false;
        input -= N * (N - 1) + 1; // Shift to 0-based vertical index
        x = input / N;
        y = input % N;
    }
}

int main(){
    bool isHorizontal; // true for horizontal, false for vertical
    int x, y;
    
    clearScreen(); // Clear the console (Windows specific)

    cout << "Welcome to the Dots and Boxes Game!\n";
    cout << "Grid size: " << N << "x" << N << "\n";
    cout << "Player R vs Player B\n";
    cout << "(1 for Horizontal line, 0 for Vertical line.)\n\n";
    
    printGrid(); // Function to print the grid
    getInput(isHorizontal, x, y);
        
    while(true){
        if (!isInsideGrid(isHorizontal, x, y)) {
            cout << "Invalid move! Try again.\n";
            getInput(isHorizontal, x, y);
            continue;
        }

        bool boxScored = updateGrid(isHorizontal, x, y, turn);
        if (!boxScored) {
            turn = (turn == 'R') ? 'B' : 'R';
        }
        
        // int prev_score = player[0] + player[1];
        // update_full(h_v, x, y, turn); // Update the grid and check for completed boxes
        // int new_score = player[0] + player[1];
        // if (new_score == prev_score) {
        //     turn = (turn == 'R') ? 'B' : 'R';
        // }
        
        if (gameFinished()) break;
        
        clearScreen(); // Clear the console (Windows specific)
        
        cout << "Welcome to the Dots and Boxes Game!\n";
        cout << "Player R: " << score[RED] << " | Player B: " << score[BLUE] << "\n\n";

        printGrid(); // Function to print the grid
        getInput(isHorizontal, x, y);
    }

    clearScreen();
    cout << "Final Score:\n";
    cout << "Player R: " << score[RED] << "\nPlayer B: " << score[BLUE] << "\n";

    printGrid();
    cout << "Game Over!\n";

    if (score[RED] > score[BLUE]) {
        cout << "Player R wins!\n";
    } else if (score[BLUE] > score[RED]) {
        cout << "Player B wins!\n";
    } else {
        cout << "It's a draw!\n";
    }
    
    return 0;
}

// g++ main.cpp -lsfml-graphics -lsfml-window -lsfml-system


/*
1 1 1
0 1 1
1 2 1
0 1 2
1 1 2
0 2 1
1 2 2
0 2 2
1 3 1
0 3 1

1 3 2
0 3 2
1 4 1
0 4 1
1 4 2
0 4 2
1 1 3
0 1 3
1 2 3
0 2 3
1 3 3
0 3 3
1 4 3
0 4 3
1 1 4
0 1 4
1 2 4
0 2 4
1 3 4
0 3 4
1 4 4
0 4 4

// Fill the bottom horizontal lines
1 5 1
1 5 2
1 5 3
1 5 4

// Fill the rightmost vertical lines
0 1 5
0 2 5
0 3 5
0 4 5
  
*/