class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        need ={}
        have = {}
        for i in range(len(list(ransomNote))):
            if ransomNote[i]not in need:
                need[ransomNote[i]]=1
            else: need[ransomNote[i]]+=1
        
        for j in range(len(list(magazine))):
            if magazine[j]not in have:
                have[magazine[j]]=1
            else: have[magazine[j]]+=1
        
        for key in need:
            if key not in have or have[key]<need[key]:
                return False
        return True
