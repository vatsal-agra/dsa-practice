class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        run = 0                                    
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                run += 1                           
                count += run
            else:
                run = 0                             
        return count