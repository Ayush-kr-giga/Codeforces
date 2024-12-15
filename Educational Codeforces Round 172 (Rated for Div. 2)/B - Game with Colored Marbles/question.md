# B. Game with Colored Marbles

## Problem Description

Alice and Bob play a game. There are \( n \) marbles, and the \( i \)-th marble has color \( c_i \). The players take turns: Alice goes first, then Bob, then Alice again, and so on.

During their turn, a player must take one of the remaining marbles and remove it from the game. If there are no marbles left (all \( n \) marbles have been taken), the game ends.

Alice's score at the end of the game is calculated as follows:
1. She receives **1 point for every color** \( x \) such that she has taken at least one marble of that color.
2. Additionally, she receives **1 point for every color** \( x \) such that she has taken **all marbles** of that color (only colors present in the game are considered).

### Example of Scoring:
Suppose there are 5 marbles with colors `[1, 3, 1, 3, 4]`:
- Alice takes the 1st marble (color 1), then Bob takes the 3rd marble (color 1), 
- Alice takes the 5th marble (color 4), then Bob takes the 2nd marble (color 3),
- Finally, Alice takes the 4th marble (color 3).

Alice's score:
- **3 points** for having at least one marble of colors \( 1, 3, 4 \),
- **1 point** for having all marbles of color \( 4 \),
- Total: **4 points**.

Alice wants to **maximize her score**, and Bob wants to **minimize it**. Both players play optimally.

## Input

- The first line contains one integer \( t \) \((1 \leq t \leq 1000)\) — the number of test cases.
- Each test case consists of two lines:
  - The first line contains one integer \( n \) \((1 \leq n \leq 1000)\) — the number of marbles.
  - The second line contains \( n \) integers \( c_1, c_2, \dots, c_n \) \((1 \leq c_i \leq n)\) — the colors of the marbles.

### Additional Constraints:
- The sum of \( n \) over all test cases does not exceed \( 1000 \).

## Output

For each test case, print one integer — Alice's score at the end of the game, assuming that both players play optimally.

