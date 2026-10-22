class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # new_str = []
        # n =len(sorted_str)
        # sorted_str = sorted(strs)
        # for i in range(len(sorted_str)):
        #     j =i+1
        #     while j<n:
        #         new_str.append([sorted_str[i]])
        #     if sorted_str[i]==sorted_str[j]:
        #         new_str.append([sorted_str[j]])
        new_str={}
        for i in range(len(strs)):
             key="".join(sorted(strs[i]))
             if key not in new_str:
                 new_str[key]=[strs[i]]
             else:
                new_str[key].append(strs[i])
        return list(new_str.values())
            




            