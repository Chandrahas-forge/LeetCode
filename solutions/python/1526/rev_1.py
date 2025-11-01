# Placeholder for revision 1 on problem 1526
from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        diff = [0]*(n+2)
        diff[0]= target[0]
        for i in range(1,n):
            diff[i] = max(target[i]-target[i-1],0)
        return sum(diff)