class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        string ={}
        has_odd = False
        for i in range(len(s)):
            if s[i]not in string:
                string[s[i]]=1
            else:string[s[i]]+=1
        

        for key in string:
            if string[key]%2==0:
                sum+= string[key]
            else:
                odd_val = string[key]
                odd_val-=1
                sum+=odd_val
                has_odd = True
                
        
        if has_odd:
             sum+=1
             return sum
        return sum
        

        
        
