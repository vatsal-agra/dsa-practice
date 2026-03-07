class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = [i for i in s]
        for i in range(len(s)):
            if s[i] == "?":
                if i == 0:
                    if s[1] == "?":
                        answer[i] = 1
                    elif int(s[1]) == 0 or int(s[1]) == 1: 
                        answer[i] = 1
                    
                    else:
                        answer[i] = 0
                elif i == 1:
                    if s[i-1] == 0:
                        answer[i] = 9
                    else:
                        answer[i] = 1
                elif i == 3:
                    answer[i] = 5
                else:
                    answer[i] = "9"
        
        return "".join(answer)