class Solution(object):
    def missingInteger(self, nums):
        total = nums[0]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                total += nums[i+1]
            else:
                break

        nums_set = set(nums)
        while total in nums_set:
            total += 1
            
        return total