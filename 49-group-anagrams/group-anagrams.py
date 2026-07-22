class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}

        for i in range(len(strs)):

            key = "".join(sorted(strs[i]))

            if key not in groups:
                groups[key] = [strs[i]]

            else:
                groups[key].append(strs[i])

        return groups.values()