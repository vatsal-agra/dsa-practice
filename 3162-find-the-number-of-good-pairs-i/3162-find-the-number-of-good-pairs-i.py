class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter

        freq = Counter(nums2)
        count = 0

        for x in nums1:
            if x % k != 0:
                continue
            target = x // k
            i=1
            while i*i <= target:
                if target % i == 0:
                    count += freq.get(i,0)
                    if i != target // i:
                        count += freq.get(target // i, 0)
                i += 1
        return count