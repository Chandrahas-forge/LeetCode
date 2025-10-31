class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
            1
          .
        10 11 12 13 14 19
        .
        100 
        dfs(1,) 
        1 000
          001
          002 
        
        1000
        """
        if n==k:
            return k
        max_len = len(str(n))
        max_possible_children_base = 0
        t= max_len-1
        while(t):
            max_possible_children_base += 10**t
            t-=1
        print(max_possible_children_base) # 110
        first_digit = -1
        for i in range(1,9):
            k-=1
            if k == 0:
                return i
            
            if k > max_possible_children_base:
                k-=max_possible_children_base
                continue
            first_digit = i
            break
        
        return self.dfs(first_digit,k,n,1,max_len)        
        
    def dfs(self,digit,k,n,curr_len,max_len):

        print(f"digit {digit} k{k} curr_len is {curr_len}")

        cm = max_len -curr_len-1 # 2 we need 10 3 - 1 = 2 -1 = > 10 1-> 1
        max_possible_children_base = 0
        curr_max_digit = str(n)[curr_len]
        while(cm):
            max_possible_children_base += 10**cm
            cm-=1
        
        print(f"Max posible children base is {max_possible_children_base}")
        
        ndigit = digit*10

        for i in range(0,10):
            k-=1
            if k==0:
                return ndigit+i
            
            if k > max_possible_children_base:
                k-=max_possible_children_base
                continue
            ndigit = ndigit+i
            break
        return self.dfs(ndigit,k,n,curr_len+1,max_len)
        

def main():
    soln = Solution()
    tc = {
        (13,2) : 10,
        (1235,345):197,
        (78043,24324):3189,
        (786,234):110,
        (786,221):298,
        (786,222):299,
        (786,223):3,
        (786,224):30,
        (786,225):300,

    }
    for key,val in tc.items():
        n,k = key
        print("**"*20)
        print(f"For n->{n} and k->{k} finding soln")

        ans = soln.findKthNumber(n,k)
        if ans!=val:
            print(f"The answer is incorrect %s expected is %s" % (ans,val))
        else:
            print(f"THe soln is as expected {ans}")
        print("**"*20)



if __name__ == "__main__":
    main()