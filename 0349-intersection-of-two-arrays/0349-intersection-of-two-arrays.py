class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = set(nums1)
        l2 = set(nums2)
        return list(l1 & l2)
