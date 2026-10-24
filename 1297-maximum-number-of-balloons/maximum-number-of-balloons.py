class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word ="balloon"
        count = float('inf')
        dict_w={}
        diction ={}
        for i in range(len(text)):
            if text[i] not in diction:
                diction[text[i]]=1
            else: diction[text[i]]+=1

        for j in range(len(word)):
            if word[j] not in dict_w:
                dict_w[word[j]]=1
            else: dict_w[word[j]]+=1
        for key in dict_w:
            if key not in diction or diction[key] < dict_w[key]:
                return 0 
        for key in dict_w:
            possible =diction[key]//dict_w[key]
            count = min (count, possible)
        return count
        
