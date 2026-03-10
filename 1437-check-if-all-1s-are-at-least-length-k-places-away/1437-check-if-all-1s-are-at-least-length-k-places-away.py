class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        
        count = k
        for i in range(len(nums)):
            if nums[i] == 1:
                if count < k:
                    return False
                count = 0
            else:
                count+=1
        return True"""

        distance = 0
        found = False
        
        for num in nums:
            if num == 1:
                
                if distance <= k and found:
                    return False 
                
                found = True

                distance = 0
            
            distance += 1

        return True