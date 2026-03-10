class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                sum += nums[i+1]
            else:
                break
        while True:
            if sum in nums:
                sum += 1
            else:
                return sum