class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_t={}
        hash_s={}
        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]]+=1
            else:
                hash_s[s[i]]=1

        for j in range(len(t)):
            if t[j] in hash_t:
                hash_t[t[j]]+=1
            else:
                hash_t[t[j]]=1
            
            sorted(hash_s.items())
            sorted(hash_t.items())

        if hash_s==hash_t :
            return True
        else:
            return False
        
        