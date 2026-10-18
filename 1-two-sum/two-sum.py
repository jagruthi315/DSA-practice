class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(nums)
        for i  in range(n):
            j=i+1
            
            while j<n:
                
                if nums[i]+nums[j]==target:
                    return [i,j]
                j+=1
            
                


            
           
