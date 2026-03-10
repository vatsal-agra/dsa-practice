class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        pivot = min(nums2)*k
        for i in range(len(nums1)):
            if nums1[i] >= pivot:
                for j in range(len(nums2)):
                    if nums1[i] % (nums2[j]*k) == 0:
                        count += 1
        return count
