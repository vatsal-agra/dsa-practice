class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {0:1}
        running = 0
        count = 0
        for i in nums:
            running = running+i
            r = running%k
            count += seen.get(r,0)
            seen[r] = seen.get(r,0)+1
        return count
