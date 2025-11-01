class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def backtrack(row_val,col_set,primary_diag_set,secondary_diag_set):

            if row_val == n:
                nonlocal count
                count +=1
                return
            
            for col_val in range(n):
                primary_diag_val = row_val-col_val
                secondary_diag_val = row_val+col_val

                if col_val in col_set or primary_diag_val in primary_diag_set or secondary_diag_val in secondary_diag_set:
                    continue
                
                col_set.add(col_val)
                primary_diag_set.add(primary_diag_val)
                secondary_diag_set.add(secondary_diag_val)
                backtrack(row_val+1,col_set,primary_diag_set,secondary_diag_set)
                col_set.remove(col_val)
                primary_diag_set.remove(primary_diag_val)
                secondary_diag_set.remove(secondary_diag_val)
            
        
        backtrack(0,set(),set(),set())
        return count

"""
Ai Commentary 

1) Forgot the return statement but the code still works (why?)
2) nonlocal avoids global mutation (is ok compared to using global keyword) but alternatives 
   exists such as using a list counter or returning int from the function 
3) Better docstrings

Alternative approaches 
1) Bitmasking
2) Permutation based 

"""
