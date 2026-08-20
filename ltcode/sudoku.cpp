#include <bits/stdc++.h>
using namespace std;

vector<vector<vector<char>>> allSolutions; // store all sudoku solutions

bool isSafe(vector<vector<char>>& board, int row, int col, char ch) {
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == ch) return false;
        if (board[i][col] == ch) return false;
        if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == ch) return false;
    }
    return true;
}

void solveSudoku(vector<vector<char>>& board) {
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (board[row][col] == '.') {  // empty cell
                for (char ch = '1'; ch <= '9'; ch++) {
                    if (isSafe(board, row, col, ch)) {
                        board[row][col] = ch;
                        solveSudoku(board); // continue searching
                        board[row][col] = '.'; // backtrack
                    }
                }
                return; // stop further check until this cell filled
            }
        }
    }
    // if we reach here -> full solution found
    allSolutions.push_back(board);
}

void printSudoku(const vector<vector<char>>& board) {
    int i = 0;
    cout << "-------------------------" << endl;
    for (const auto& row : board) {
        int j = 0;
        cout << "| ";
        for (char cell : row) {
            cout << cell << " ";
            if (j == 2 || j == 5) cout << "| ";
            j++;
        }
        cout << "|" << endl;
        if(i == 2 || i == 5)
            cout << "--------+-------+--------" << endl;
        i++;
    }
    cout << "-------------------------" << endl;
}

bool isValidSudoku(vector<vector<char>>& board) {
    vector<char> v;
    for (int i = 0; i < 9; i++) {
        v = {'1','2','3','4','5','6','7','8','9'};
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') continue;
            auto it = find(v.begin(), v.end(), board[i][j]);               
            if (it != v.end()) v.erase(it);
            else return false;
        }

        v = {'1','2','3','4','5','6','7','8','9'};
        for (int j = 0; j < 9; j++) {
            if (board[j][i] == '.') continue;
            auto it = find(v.begin(), v.end(), board[j][i]);               
            if (it != v.end()) v.erase(it);
            else return false;
        }
        
        v = {'1','2','3','4','5','6','7','8','9'};
        int a = (i/3)*3, b = (i%3)*3;
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if (board[a+j][b+k] == '.') continue;
                auto it = find(v.begin(), v.end(), board[a+j][b+k]);               
                if (it != v.end()) v.erase(it);
                else return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','.','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','.','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','.'}
    };

    cout << "Sudoku Puzzle:" << endl;
    printSudoku(board);

    if (isValidSudoku(board)) {
        solveSudoku(board);

        cout << "\nTotal Solutions Found: " << allSolutions.size() << "\n\n";
        int count = 1;
        for (auto& sol : allSolutions) {
            cout << "Solution #" << count++ << ":\n";
            printSudoku(sol);
            cout << "\n";
        }
    }
    else {
        cout << "Sudoku is invalid." << endl;
    }
    return 0;
}
// This code solves a Sudoku puzzle and prints all possible solutions.
// It checks for validity, uses backtracking to find solutions, and formats the output nicely.