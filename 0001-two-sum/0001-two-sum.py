class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        sum = 0
        a = 0
        b = len(nums)-1
        for i in range(len(nums)-1):
            while a < b:
                if nums[a]+nums[b] == target:
                    ans.append(a)
                    ans.append(b)
                a += 1
            b -= 1
            a = 0
        return ans