# N‑Queens II · LeetCode 52

The **N‑Queens puzzle** asks for ways to place `n` queens on an `n × n` chessboard so that no two queens attack each other (no two share a row, column, or diagonal).

Given an integer&nbsp;`n`, **return the number of distinct solutions** to the puzzle.

---

## Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `n = 4` | `2` | There are exactly two valid 4‑queen arrangements. |
| `n = 1` | `1` | The single queen occupies the only square. |

---

## Constraints

* `1 ≤ n ≤ 9`

---

## Hints / Suggested Approaches (links)

* Backtracking with pruning  
* Bit‑mask optimisation (treat columns and diagonals as bitsets)

---

> **Original prompt:** [LeetCode 52 – “N‑Queens II”](https://leetcode.com/problems/n-queens-ii/)
