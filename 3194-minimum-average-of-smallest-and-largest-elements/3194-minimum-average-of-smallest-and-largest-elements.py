class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages = []
        for i in range(len(nums)/2):
            averages.append((float(max(nums)+min(nums))/2))
            nums.remove(max(nums))
            nums.remove(min(nums))


        return min(averages)