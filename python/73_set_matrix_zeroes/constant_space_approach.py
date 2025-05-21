class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        if matrix[0][0]==0:
            first_row_zero = True
            first_col_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                matrix[0][0]= "#"
                matrix[i][0]="#"
                first_col_zero = True
                
        for j in range(n):
            if matrix[0][j] == 0:
                matrix[0][j] = "#"
                first_row_zero = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]="#"
                    matrix[0][j]= "#"
        
        for i in range(1,m):
            if matrix[i][0] != "#":
                continue
            
            for j in range(n):
                matrix[i][j]=0
        
        for j in range(1,n):
            if matrix[0][j] !="#":
                continue
            
            for i in range(m):
                matrix[i][j] =0
        
        if first_row_zero:
            for j in range(n):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(m):
                matrix[i][0]= 0
        
        return matrix

"""
AI Commentary

1) Remove extra marker # and can be replaced with zero 
2) set boolean flags (first row and first column) with any generator approach
3) row assignement of zeroes can be done as matrix[i] = [0]*n(cleaner)
"""