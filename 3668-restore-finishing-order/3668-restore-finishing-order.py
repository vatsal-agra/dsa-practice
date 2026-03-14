class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in order:
            if i in friends:
                answer.append(i)
        return answer