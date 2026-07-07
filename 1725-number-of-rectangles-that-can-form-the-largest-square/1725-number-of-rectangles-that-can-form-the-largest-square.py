class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        '''greatest = 0
        for i in rectangles:
            if min(i) > greatest:
                greatest = min(i)
        
        for i in rectangles:
            if min(i) == greatest:
                count = count + 1

        return count'''
        count = 0
        rectangles.sort()
        for i in rectangles:
            if min(i) == min(rectangles[-1]):
                count = count + 1

        return count