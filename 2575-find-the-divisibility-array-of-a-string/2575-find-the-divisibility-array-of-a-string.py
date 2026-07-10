class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        sum = 0
        ans = []
        for i in word:
            sum = (sum%m)*10+int(i)
            if sum%m == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans