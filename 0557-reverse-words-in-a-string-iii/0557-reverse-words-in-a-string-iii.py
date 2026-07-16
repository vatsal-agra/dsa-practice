class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        check = s.split(" ")
        ans = []
        for i in check:
            word = list(i)
            a=0
            b=len(i)-1
            while a < b:
                word[a], word[b] = word[b], word[a]
                a += 1
                b -= 1
            ans.append("".join(word))
        return " ".join(ans)
