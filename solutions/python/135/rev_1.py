class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        3 4 5 4 3 2 1 
        asc = 3 
        dsc = 4
        sum = 1+2+3+1+2+3+4 = 16
        dsc+1-asc
        sum += 

        1 2 3 2 1
        asc=3

        asc = 3
        dsc = 5
        1 2 87 87 2 1 
        

        1 + 2 + 3= 6
        1+2+3+4+5 = 15 
        so 5 gets asc extra so 21-3=18

        """
        n=len(ratings)
        dpf = [1]*n
        dpb = [1]*n
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                dpf[i]=dpf[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                dpb[i]=dpb[i+1]+1

        # print(dpf)
        # print(dpb)
        ans=0
        for i in range(n):
            ans += max(dpf[i],dpb[i])
        return ans
