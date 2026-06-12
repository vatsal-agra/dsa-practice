class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > min(nums):
            return -1

        else:
            count = 0
            nums.sort()
            for i in range(len(nums)-1):
                if nums[(len(nums)-1) - (i+1)] < nums[(len(nums)-1)-i]:
                    count = count + 1

            return count if k==min(nums) else count+1