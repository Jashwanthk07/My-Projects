##Tic Tac Toe (Python)
#Overview

This is a simple command-line Tic Tac Toe game built in Python using functions and logical operations.
The game allows two players (X and O) to take turns placing their symbols on a 3x3 grid. It checks for wins across rows, columns, and diagonals after each move and declares the winner or a draw accordingly.

#Features

Two-player mode (X and O)

Input validation for correct row and column entries

Win detection across:
Rows
Columns
Both diagonals

 Displays board after every move

 Declares winner or draw automatically

#Tech Stack

Language: Python

Library Used: numpy (for easy matrix/array handling)

#How It Works

The board is represented as a 3x3 NumPy array.

Players take turns to enter their move (row and column).

After every move:

The program checks for 3 consecutive identical symbols in any row, column, or diagonal.

If found → declares a winner.

If all cells are filled and no winner → declares a draw.

#Sample Gameplay
[['-' '-' '-']
 ['-' '-' '-']
 ['-' '-' '-']]
X turn
Enter the row -1 or 2 or 3: 1
Enter the column- 1 or 2 or 3: 1

[['X' '-' '-']
 ['-' '-' '-']
 ['-' '-' '-']]
O turn
Enter the row -1 or 2 or 3: 2
Enter the column- 1 or 2 or 3: 1
...
X Wins

#How to Run

Install Python 3.x

Install NumPy (if not already installed):

pip install numpy


Run the script:

python tic_tac_toe.py

#Learning Highlights

Functional programming approach in Python

Logic-based flow for game design

Input validation and condition handling

Use of 2D arrays with NumPy

#Future Enhancements

Add AI opponent (using Minimax algorithm)

Implement a Graphical User Interface (GUI) using tkinter or pygame

Add score tracking and replay option

#Author
Ch Jashwanth Kumar
B.E. in Artificial Intelligence and Data Science
Chaitanya Bharathi Institute of Technology (CBIT), Hyderabad
