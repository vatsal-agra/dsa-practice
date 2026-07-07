class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        greatest = 0
        for i in rectangles:
            if min(i) > greatest:
                greatest = min(i)
        count = 0
        for i in rectangles:
            if min(i) == greatest:
                count = count + 1

        return count