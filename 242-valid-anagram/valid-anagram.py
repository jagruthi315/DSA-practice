class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
 

        if len(s) != len(t):
            return False

        freq = {}
        freq2 = {}

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in freq2:
                freq2[t[j]] = 1
            else:
                freq2[t[j]] += 1

        return freq == freq2
        