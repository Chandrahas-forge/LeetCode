# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        def merge(list1,list2):

            if list1 is None:
                return list2
            
            if list2 is None:
                return list1
        
            if list1.val < list2.val:
                list1.next = merge(list1.next,list2)
                return list1
        
            list2.next = merge(list1,list2.next)
            return list2
        
        n = len(lists)
        while(n!=1):
            new_lists = []
            for i in range(0,n,2):
                if i+1 < n:
                    new_lists.append(merge(lists[i],lists[i+1]))
                else:
                    new_lists.append(lists[i])
            lists=new_lists
            n = len(lists)
        
        return lists[0]

"""
Ai Commentary
In summary, you can make your existing code more idiomatic and maintainable by filtering out empty lists early, 
replacing recursion with an iterative two-list merge, 
using a list comprehension to pair up lists, 
and adding type hints plus clear naming per the Zen of Python. 
Beyond that, alternative approaches include a 
1) min-heap (priority queue) merge, 
2) a tournament-tree (loser-tree) merge, 
3) leveraging Python’s built-in heapq.merge() for lazy merging, 
4) adaptive merges like Powersort
"""
        


