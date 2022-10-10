class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) #finding the number of rows.
        n = len(matrix[0]) #finding the number of columns. 
        
        #after finding the number of rows and columns now we have to initialize the two pointers. 
        
        low = 0 #low is my first index
        high = (m*n)-1 #high is my last index in the matrix. 
        
        while low<=high:
            
            mid = low+(high-low)//2 #to avoid integer over flow, this is how we have to find the mid. 
            
            num = matrix[mid//n][mid%n]
            
            
            if num == target:   #if mid equal to target we are returning true
                return True
            
            elif num>target: #f the mid is less than the target we are moving the high pointer to mid -1
                high = mid -1
                
            else:            # if the mid is less than the target we are moving the low pointer to mid+1
                low = mid+1
                
        return False

        