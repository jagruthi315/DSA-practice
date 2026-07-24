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

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1

            if t[i] not in freq:
                freq[t[i]] = -1
            else:
                freq[t[i]] -= 1

        for value in freq.values():
            if value != 0:
                return False

        return True
        