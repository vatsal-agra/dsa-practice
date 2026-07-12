class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                ans = max(ans, count)   # check the max right here, every step
            else:
                count = 0
        return ans