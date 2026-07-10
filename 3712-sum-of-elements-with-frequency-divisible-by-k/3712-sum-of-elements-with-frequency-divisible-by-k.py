class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        check = {}
        sum = 0
        for i in nums:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        for i in check:
            freq = check.get(i)
            if freq%k == 0:
                sum += i*freq
        return sum