import heapq
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        x1 x2 | x3 x4 x5 x6

        x1+x1 x2+x2 x3+x3 x4+x4 x5+x5 x6+x6
        x1+x2 x3+x5
        x2+x3 

        2 4 6 2
        - 6 8 4
        - - 10 6
        - - - 2

        x1 and x6 will always be there now for k bags we need


        """
        if k==1:
            return 0
        n=len(weights)
        mp = []
        maxp=[]
        for i in range(n-1):
            s = weights[i]+weights[i+1]
            heapq.heappush(mp,s)
            heapq.heappush(maxp,-s)
        k-=1
        msum=weights[0]+weights[-1]
        masum = msum
        # print(mp)
        # print(maxp)
        while(k):
            msum+=heapq.heappop(mp)
            masum-=heapq.heappop(maxp)
            k-=1
        
        return masum-msum
    





        
