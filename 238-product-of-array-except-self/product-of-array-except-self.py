class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
       
        leftproduct = 1
        rightproduct = 1

        for i in range(len(nums)):
            answer.append(leftproduct)
            leftproduct =leftproduct*nums[i]

        for j in range(len(nums)-1,-1,-1):

            answer[j] *= rightproduct 
            rightproduct *= nums[j]
        return answer

