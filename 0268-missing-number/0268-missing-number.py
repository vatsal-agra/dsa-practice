class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = len(set(nums))
        for i in range(dist+1):
            if i not in nums:
                return i
        