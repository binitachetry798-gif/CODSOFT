# Tic Tac Toe - AI Game (Console Version)

An intelligent Tic Tac Toe game where you play against an AI opponent in the console. The AI uses the **Minimax algorithm** to play optimally and is virtually unbeatable.

## Features

- **Play vs AI**: Challenge an intelligent computer opponent
- **Minimax Algorithm**: AI uses optimal game theory to make unbeatable moves
- **Console Interface**: Simple text-based board display
- **Input Validation**: Handles invalid inputs gracefully
- **Game Status**: Real-time feedback on game state (win, loss, draw)
- **Easy to Play**: Just enter numbers 1-9 to make your move

## Requirements

- Python 3.x
- No external dependencies (uses only built-in `math` module)

## Installation

1. Clone or download this repository
2. Ensure Python 3 is installed on your system

## How to Run

Navigate to the project directory and run:

```bash
python TIC-TAC-TOE
```

## How to Play

1. Run the game - you will be **X** and the AI will be **O**
2. The board positions are numbered 1-9:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
3. Enter a number between 1-9 to place your X
4. The AI automatically makes its O move
5. Continue alternating until someone wins or the board is full
6. **You move first!**

## Game Rules

- You are X and move first
- AI opponent is O and moves second
- Win by getting 3 of your symbols in a row (horizontal, vertical, or diagonal)
- If all 9 cells are filled with no winner, it's a draw
- Each cell can only be filled once
- Invalid moves will prompt you to try again

## Board Display

The game prints a 3x3 grid showing the current board state. Empty cells show positions 1-9, X shows your moves, and O shows the AI's moves.

## AI Algorithm: Minimax

The AI uses the Minimax algorithm, a decision-making strategy that:
- Evaluates all possible future moves
- Scores each move based on win/loss/draw outcomes
- Always chooses the move with the best outcome
- Makes the AI virtually unbeatable

## Files

- `TIC-TAC-TOE` - Main game file with AI opponent

## Example Game Session

```
Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.
 | |
-----
 | |
-----
 | |

Enter your move (1-9): 5
 | |
-----
 |X|
-----
 | |

AI played:
O| |
-----
 |X|
-----
 | |
```

## Difficulty

The AI is set to **Hard difficulty** - it will not lose games against human players. At best, you can achieve a draw if you play perfectly.

## Tips for Players

- The center (position 5) is often a strong opening response
- Try to create two winning threats simultaneously
- Block the AI when it's one move away from winning
- Even perfect play will likely result in a draw against this AI

---

Enjoy the challenge!
