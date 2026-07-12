class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nxt = {}                              # ← the hashmap
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                nxt[stack.pop()] = num        # ← writing to it
            stack.append(num)
        return [nxt.get(x, -1) for x in nums1] 