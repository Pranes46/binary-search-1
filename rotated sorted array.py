class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0 # we gonna use two pointers to solve this prob, initializing low pointer to the index 0
        high = len(nums)-1
        
        while low<=high:
            mid = low+(high-low)//2 #to avoid integer over flow, this is how we gonna find mid.
            
            if nums[mid]==target: #if target is equals to mid return the mid
                return mid
            
            if nums[low] <= nums[mid]: #to check whether the left side is sorted
                
                if target>=nums[low] and nums[mid] > target: # to check whether the target is between the low and the mid.
                    high = mid - 1 # if it is between the low and mid we are moving the high pointer to mid-1
                    
                else:
                    low = mid + 1 #if it does not lie under the low and mid we are moving the low pointer to mid +1
                    
            else: #right sorted
                
                if target>nums[mid] and nums[high] >= target:
                    low = mid + 1
                    
                else:
                    high = mid -1
                    
        return -1
                
                    
                
                    
                
        