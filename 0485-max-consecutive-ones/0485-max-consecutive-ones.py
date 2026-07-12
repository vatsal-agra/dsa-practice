class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                if count>ans:
                    ans = count
                count = 0
        return ans if ans>count else count