class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        count = len(candyType)/2
        check = len(set(candyType))
        if check < count:
            return check
        else:
            return count
