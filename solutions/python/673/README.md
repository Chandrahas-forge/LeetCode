# Number of Longest Increasing Subsequence (LIS)

## Problem Description
Given an integer array `nums`, return the number of longest increasing subsequences.

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. An **increasing subsequence** is a subsequence where each element is strictly greater than the previous one.

You need to find:
1. The length of the longest increasing subsequence.
2. The count of all subsequences in `nums` that have this maximum length.

## Example

```
Input: nums = [1, 3, 5, 4, 7]
Output: 2
Explanation: The longest increasing subsequence has length 4, and there are two such subsequences:
             [1, 3, 4, 7] and [1, 3, 5, 7].
```

## Constraints
- `1 <= nums.length <= 2000`
- `-10^6 <= nums[i] <= 10^6`

