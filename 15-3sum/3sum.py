class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        i=0
      
        
        n = len(nums)
     
        res =[]
       

        for i in range(len(nums)-2):
            left =i+1
            right = n-1
            
            if i>0 and nums[i-1]==nums[i]:

                continue
  
            suma =-1*nums[i]
            while (left< right):
                val =[nums[i],nums[left],nums[right]]  
                s=nums[left]+nums[right]
                if(s==suma):
                    
                    res.append(val)
                    
                    left+=1
                    right-=1
                    while(left<n-1 and nums[left]==nums[left-1]):
                        left+=1
                    while(right>0 and nums[right]==nums[right+1]):
                        right-=1

                elif(s<suma):
                     left+=1
                else:
                    right-=1
        return res
            



     