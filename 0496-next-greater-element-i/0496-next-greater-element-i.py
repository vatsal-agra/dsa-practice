class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums1:
            j = nums2.index(i)
            for x in nums2[j+1:]:
                if x > i:
                    ans.append(x)
                    break
            else:                 
                    ans.append(-1)
        return ans