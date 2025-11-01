class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def get_base_10_val_str(base_k_str):
            value = 0
            kpow=0
            for i in range(len(base_k_str)-1,-1,-1):
                value += int(base_k_str[i])*(k**kpow)
                kpow+=1
            return str(value)
        
        def generate_next_list(current_list):
            """
            1 3  5 7
            1 
            0
            mid = 0//2=0


            3
            012
            mid = 3//2 = 1

            101
            1001
            232
            2332

            2 4 6 8
            0 1
            mid = 1


            0 1 2 3
            mid = 2
            value[0:mid] + k + value[mid:]
             
            """
            n = len(current_list[0])
            new_set = set()
            mid = n//2
            if n%2==1:
                
                for value in current_list:
                    new_set.add( value[:mid]+value[mid]+value[mid]+value[mid+1:])
            else:
                for value in current_list:
                    for i in range(k):
                        new_set.add(value[:mid] + str(i) + value[mid:])
            return sorted(list(new_set))
        def check_palindrome(val):
            low = 0
            high = len(val)-1
            while(low<high):
                if val[low]!=val[high]:
                    return False
                low+=1
                high-=1
            return True
                

        print(get_base_10_val_str("110"))
        base_k_mirror = [str(i) for i in range(1,k)]
        ans=0
        while(n):
            for number in base_k_mirror:
                base_10_str = get_base_10_val_str(number)
                if check_palindrome(base_10_str):
                    # print(f"{base_10_str} is palindrome")
                    n-=1
                    ans += int(base_10_str)
                    if n==0:
                        break
            
            if n==0:
                break

            base_k_mirror = generate_next_list(base_k_mirror)
            # print(base_k_mirror)
        return ans
