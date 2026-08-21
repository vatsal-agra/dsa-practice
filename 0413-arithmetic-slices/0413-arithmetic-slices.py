class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            a = i
            b = a+1
            while b < len(nums)-1 and (nums[b] - nums[a] == nums[b+1] - nums[b]):
                count += 1
                a += 1
                b += 1

        return count

