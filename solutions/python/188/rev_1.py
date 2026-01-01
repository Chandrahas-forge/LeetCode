from functools import lru_cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(i,bought,k):

            if i==len(prices):
                if bought:
                    return float('-inf')
                else:
                    return 0
            
            if k==0:
                return 0
            
            if bought:
                o1 = dfs(i+1,bought,k)
                o2 = prices[i]+ dfs(i+1,False,k-1)
            else:
                o1 = -prices[i]+dfs(i+1,True,k)
                o2 = dfs(i+1,False,k)
            return max(o1,o2)
        
        return dfs(0,False,k)

        
