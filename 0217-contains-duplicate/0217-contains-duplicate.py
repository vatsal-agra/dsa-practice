class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 1
            else:
                return True
        return False