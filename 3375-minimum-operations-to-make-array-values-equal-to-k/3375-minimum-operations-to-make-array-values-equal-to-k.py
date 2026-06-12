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
            check = len(nums)-1
            count = 0
            nums.sort()
            for i in range(check):
                if nums[check - (i+1)] < nums[check-i]:
                    count = count + 1

            return count if k==min(nums) else count+1