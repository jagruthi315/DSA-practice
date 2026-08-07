class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        offi= 0 
        cm =1 
        res=1 
        n = len(nums)
        while (cm<n):
            if nums[cm]==nums[cm-1]:
            
                cm+=1
                continue
        
            if nums[cm]!= nums[cm-1]:
                 nums[offi+1]=nums[cm]
                 offi+=1
                 res+=1
                 cm+=1

        return res
        