class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
    
        for i in range(len(nums)):
            val = lambda x:x*x
            res.append(val(nums[i]))
        
        return sorted(res)
