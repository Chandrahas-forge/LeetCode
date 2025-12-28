from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        rgraph = {i:[] for i in range(k)}
        cgraph = {i:[] for i in range(k)}
        rde = {i:0 for i in range(k)}
        cde = {i:0 for i in range(k)}
        
        for s,d in rowConditions:
            s-=1
            d-=1
            rgraph[s].append(d)
            rde[d]+=1
        for s,d in colConditions:
            s-=1
            d-=1
            cgraph[s].append(d)
            cde[d]+=1
                
        print(rgraph)
        print(cgraph)
        print(rde)
        print(cde)
        rtop_sort = []
        ctop_sort = []

        rq = deque([k for k,v in rde.items() if v==0])
        cq = deque([k for k,v in cde.items() if v==0])
        print(rq)
        print(cq)
        while(rq):
            node = rq.popleft()
            rtop_sort.append(node)
            for child in rgraph[node]:
                rde[child]-=1
                if rde[child]==0:
                    rq.append(child)
        if len(rtop_sort) <k:
            return []
        
        print(rtop_sort)
        while(cq):
            node = cq.popleft()
            ctop_sort.append(node)
            for child in cgraph[node]:
                cde[child]-=1
                if cde[child]==0:
                    cq.append(child)
        if len(ctop_sort) <k:
            return []
        ans = [[0]*k for _ in range(k)]
        print(ans)
        print(ctop_sort)
        cimap = {}
        for i, val in enumerate(ctop_sort):
            cimap[val]=i
        
        for rowi,val in enumerate(rtop_sort):
            ans[rowi][cimap[val]]=val+1
        return ans


