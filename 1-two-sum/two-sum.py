class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
            
        dicton={}
        for  i in range(len(nums)):
         
            if target - nums[i] in dicton:
        
                return[i, dicton[target-nums[i]]]
            else:
                dicton[nums[i]] = i
        return "not found"
                


            
           
