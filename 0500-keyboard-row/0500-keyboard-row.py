class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        ans = []
        print r2
        for i in words:
            check = set(i.lower())
            if check.issubset(r1) or check.issubset(r2) or check.issubset(r3):
                ans.append(i)
        return ans