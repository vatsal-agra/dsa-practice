class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i in nums1:
            count = 0
            hi = True
            check = nums2.index(i)
            while hi:
                count += 1
                if check+count < len(nums2):
                    if nums2[check+count] > i:
                        ans.append(nums2[check+count])
                        hi = False
                else:
                    ans.append(-1)
                    hi = False
        return ans