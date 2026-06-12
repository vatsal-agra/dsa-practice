class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        highest = max(nums)
        nums.sort()
        for i in range(len(nums)-1):
            summ = summ + highest-nums[i]
        return summ