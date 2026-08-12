# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         closest_sum =0
#         n = len(nums)
       
#         min_diff = float('inf')
    
#         for i in range(n-2):
#             left =i+1
#             right = n-1
            
#             while(left< right):
            
#                 suma =nums[i]+nums[left]+nums[right]
#                 diff=abs(target-suma)
#                 if min_diff>diff:
                    
#                   min_diff =diff
#                   closest_suma =suma

#                   if(closest_suma == target ):
#                      return suma

#                   elif (suma<target):
#                      left+=1
                
#                   else:right-=1



class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = len(nums)

        min_diff = float('inf')
        closest_suma = 0

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                suma = nums[i] + nums[left] + nums[right]
                diff = abs(target - suma)

                # Save the closest sum
                if diff < min_diff:
                    min_diff = diff
                    closest_suma = suma

                # Exact match = closest possible
                if suma == target:
                    return suma

                elif suma < target:
                    left += 1

                else:
                    right -= 1

        return closest_suma     
            


