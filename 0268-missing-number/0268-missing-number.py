class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = len(set(nums))
        print set(nums),dist
        for i in range(dist+1):
            if i not in nums:
                return i
        