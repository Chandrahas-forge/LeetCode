# 23 Merge k Sorted Lists

[LeetCode Problem](https://leetcode.com/problems/merge-k-sorted-lists)

## Problem Statement

You are given an array of k linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Constraints

- `k == len(lists)`  
- `0 <= k <= 10^4`  
- `0 <= lists[i].length <= 500`  
- `-10^4 <= lists[i][j] <= 10^4`  
- `lists[i]` is sorted in ascending order.  
- The total number of nodes across all lists will not exceed `10^4`.

## Examples

**Example 1:**
```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```
_Explanation:_  
The linked-lists are:
```text
1->4->5,
1->3->4,
2->6
```
Merging them into one sorted list: `1->1->2->3->4->4->5->6`

**Example 2:**
```text
Input: lists = []
Output: []
```

**Example 3:**
```text
Input: lists = [[]]
Output: []
```


