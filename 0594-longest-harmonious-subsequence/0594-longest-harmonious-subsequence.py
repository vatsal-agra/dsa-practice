from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        best = 0
        for x in count:
            if x + 1 in count:
                best = max(best, count[x] + count[x + 1])
        return best