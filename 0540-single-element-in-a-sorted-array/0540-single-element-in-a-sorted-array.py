class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        top = len(nums)-1
        bottom = 0
        while True:
            n = bottom + (top - bottom)//2
            leftDiff = (n == 0) or nums[n] != nums[n-1]
            rightDiff = (n == len(nums)-1) or nums[n] != nums[n+1]
            if leftDiff and rightDiff:
                return nums[n]
            if n%2 == 0:
                if nums[n+1] != nums[n]:
                    top = n-1
                else:
                    bottom = n+1
            else:
                if nums[n-1] != nums[n]:
                    top = n-1
                else:
                    bottom = n+1