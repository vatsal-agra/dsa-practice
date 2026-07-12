class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = set(nums)
        answer = []
        for i in range(1,len(nums)+1):
            if i not in check:
                answer.append(i)

        return answer