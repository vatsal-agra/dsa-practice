class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        se = set(nums)
        dist = len(se)
        for i in range(dist+1):
            if i not in se:
                return i
        