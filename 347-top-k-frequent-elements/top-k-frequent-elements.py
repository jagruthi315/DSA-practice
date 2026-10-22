class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new_nums={}
        count = 0 
        for i in range(len(nums)):
        
            if nums[i] not in new_nums:
                count =1
                new_nums[nums[i]]=count
            else:
                new_nums[nums[i]]+=1
            
        new_vals = sorted(new_nums.items() ,key = lambda x:x[1] , reverse = True)
        return [item[0] for item in new_vals[:k]]

            
