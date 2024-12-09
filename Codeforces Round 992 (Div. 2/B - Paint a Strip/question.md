# Problem Statement

You are given an array of zeros `a = [0, 0, ..., 0]` of length `n`.

You can perform two types of operations on the array:

1. **First Type**:
   - Choose an index `i` such that `1 ≤ i ≤ n` and `a[i] = 0`.
   - Assign `a[i] = 1`.

2. **Second Type**:
   - Choose a pair of indices `l` and `r` such that `1 ≤ l ≤ r ≤ n` and:
     - `a[l] = 1`.
     - `a[l] + a[l+1] + ... + a[r] = r - l + 1` (all elements between `l` and `r` inclusive are `1`).
   - Assign `a[r+1] = 1`.

Your task is to determine the **minimum number of operations of the first type** required to make all elements of the array equal to `1`.

---

## Input

The input consists of multiple test cases:

- The first line contains the number of test cases `t` (`1 ≤ t ≤ 10^4`).
- Each of the next `t` lines contains one integer `n` (`1 ≤ n ≤ 10^5`) — the length of the array for that test case.

It is guaranteed that the total sum of all `n` across test cases does not exceed `10^5`.

---

## Output

For each test case, print a single integer — the minimum number of operations of the **first type** required.

---
