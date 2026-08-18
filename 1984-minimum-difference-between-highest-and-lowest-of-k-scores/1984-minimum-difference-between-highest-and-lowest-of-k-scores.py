class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        check = float('inf')                     
        for i in range(len(nums) - k + 1):     
            check = min(check, nums[i + k - 1] - nums[i])   
        return check
        