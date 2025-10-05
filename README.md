# Tic Tac Toe (Python)

A simple, clean **command-line Tic Tac Toe** game built in Python.  
Two players (X and O) take turns on a 3×3 grid.  
After each move, the game checks rows, columns, and diagonals for a win—or declares a draw when the board is full.

---

## Overview

This project is a beginner-friendly implementation of the classic Tic Tac Toe game using Python.  
It’s designed to help understand logic-based game design, input handling, and use of NumPy arrays.

- Turn-based, two-player gameplay (X and O)
- Clear board rendering after every move
- **Input validation** for correct entries (1–3)
- **Win detection** across:
  - Rows  
  - Columns  
  - Both diagonals  
- Automatic **winner/draw** announcement

---

## Features

- Two-player mode (X and O)  
- Input validation for row and column entries  
- Win detection across:
  - Rows  
  - Columns  
  - Main and anti-diagonal  
- Displays the board after every move  
- Declares **winner** or **draw** automatically  

---

## Tech Stack

- **Language:** Python 3.x  
- **Library Used:** `numpy` (for easy matrix/array handling)

---

## How It Works

1. The board is represented as a **3×3 NumPy array** filled with `'-'` (empty).
2. Players take turns entering **row** and **column** numbers (`1`, `2`, or `3`).
3. After each move:
   - The program checks all rows, columns, and diagonals.
   - If any of them contain three identical symbols (`X` or `O`), a **winner** is declared.
   - If all cells are filled and no winner exists, the game ends in a **draw**.
4. The board is printed after every move to show progress.

---

## Sample Gameplay
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


---

## Installation & Run Instructions

### Step 1: Install Python
Make sure you have **Python 3.x** installed.  
Check using:
```bash
python --version
```
###Step 2: Install NumPy

If you don’t already have NumPy, install it with:

pip install numpy

###Step 3: Run the Game

Navigate to your project folder and run:
```
python tic_tac_toe.py

```
or (on some systems)
```
python3 tic_tac_toe.py
```

## Requirements 
```
numpy>=1.20
```

## How to Play

- Run the script in your terminal or IDE.

-cThe board will display as a 3×3 grid with '-' for empty cells.

- Player X goes first.

- Enter your desired row and column (1–3).

- The program automatically checks for a winner or draw after each move.

- Keep playing until:

- One player wins 🎉

- Or all cells are filled → It’s a draw 🤝

## Author
Ch Jashwanth 
