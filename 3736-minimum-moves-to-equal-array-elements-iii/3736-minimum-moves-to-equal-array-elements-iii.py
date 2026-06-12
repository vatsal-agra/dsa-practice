class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        highest = max(nums)
        for i in nums:
            if i != highest:
                summ = summ + highest-i
        return summ