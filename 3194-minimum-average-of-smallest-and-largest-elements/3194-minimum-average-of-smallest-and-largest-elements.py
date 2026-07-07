class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages = []
        nums.sort()
        n = len(nums)
        for i in range(n/2):
            averages.append(((nums[i]+nums[n-i-1])/2.0))
           

        return min(averages)