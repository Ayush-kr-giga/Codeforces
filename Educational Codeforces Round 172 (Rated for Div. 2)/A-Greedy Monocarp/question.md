# A. Greedy Monocarp

## Problem Description

There are \( n \) chests; the \( i \)-th chest initially contains \( a_i \) coins. For each chest, you can choose any non-negative (0 or greater) number of coins to add to that chest, with one constraint: the total number of coins in all chests must become at least \( k \).

After you've finished adding coins to the chests, greedy Monocarp comes, who wants the coins. He will take the chests one by one, and since he is greedy, he will always choose the chest with the maximum number of coins. Monocarp will stop as soon as the total number of coins in chests he takes is at least \( k \).

You want Monocarp to take as few coins as possible, so you have to add coins to the chests in such a way that, when Monocarp stops taking chests, he will have exactly \( k \) coins. Calculate the minimum number of coins you have to add.

## Input

The first line contains one integer \( t \) \((1 \leq t \leq 1000)\) — the number of test cases.

Each test case consists of two lines:
- The first line contains two integers \( n \) and \( k \) \((1 \leq n \leq 50; 1 \leq k \leq 10^7)\);
- The second line contains \( n \) integers \( a_1, a_2, \dots, a_n \) \((1 \leq a_i \leq k)\).

## Output

For each test case, print one integer — the minimum number of coins you have to add so that, when Monocarp stops taking the chests, he has exactly \( k \) coins. It can be shown that under the constraints of the problem, it is always possible.

