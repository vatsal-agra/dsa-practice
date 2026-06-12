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
            check = []
            for i in nums:
                if i not in check:
                    check.append(i)
            return len(check)-1 if min(nums) == k else len(check) 