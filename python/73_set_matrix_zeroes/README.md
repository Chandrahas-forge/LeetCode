# 73. Set Matrix Zeroes

## Problem Description
Given an m x n integer matrix `matrix`, if an element is 0, set its entire row and column to 0's.
You must do it **in-place**.

## Examples

**Example 1:**
```
Input:
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

**Example 2:**
```
Input:
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

## Constraints
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^{31} <= matrix[i][j] <= 2^{31} - 1`

## Follow-up
1. A straightforward solution using O(m·n) extra space is a bad idea.
2. A simple improvement uses O(m + n) extra space, but still not the best solution.
3. Can you devise a **constant space** solution?


