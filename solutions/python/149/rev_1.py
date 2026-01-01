from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        sd = defaultdict(set)
        if len(points)==1:
            return 1
        
        for i,p1 in enumerate(points):
            for j in range(i+1,len(points)):
                x1,y1 = p1
                x2,y2 = points[j]
                if x1==x2:
                    slope=float('inf')
                    c = x1
                else:
                    slope = (y2-y1)/(x2-x1)
                    c=y2-slope*x2
                t = (slope,c)
                sd[t].add(tuple(p1))
                sd[t].add(tuple(points[j]))
        ml=2
        for k,v in sd.items():
            ml = len(v) if len(v)>ml else ml
        return ml
                




        
