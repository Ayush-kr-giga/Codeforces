# Problem Statement

You are given an array of integers `a` of length `n` and an integer `k`.

Two players are playing a game:
1. The **first player** chooses an index `1 ≤ i ≤ n`.
2. The **second player** chooses a different index `1 ≤ j ≤ n` (`j ≠ i`).

The **first player wins** if `a[i]` is **not divisible** by `a[j] % k`. Otherwise, the **second player wins**.

Your task is to determine if it is possible for the **first player to win**, and if so, which index `i` should the first player choose.

---

## Input

The input consists of multiple test cases:

- The first line contains a single integer `t` (`1 ≤ t ≤ 100`) — the number of test cases.
- The description of each test case follows:
  - The first line contains two integers `n` and `k` (`1 ≤ n ≤ 100; 1 ≤ k ≤ 100`) — the length of the array and the divisor value `k`.
  - The second line contains `n` integers `a[1], a[2], ..., a[n]` (`1 ≤ |a[i]| ≤ 100`) — the elements of the array.

---

## Output

For each test case:

- If it is impossible for the **first player to win**, print `"NO"` (without quotes).
- Otherwise, print `"YES"` (without quotes) on one line, and on the next line, print the index `1 ≤ i ≤ n` that the **first player** should choose.

If there are multiple valid solutions, you can print any of them.

You can output each letter in any case (e.g., `"yes"`, `"Yes"`, and `"YES"` are all valid).

---