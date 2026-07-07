class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        best = count = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > best:
                best, count = side, 1
            elif side == best:
                count += 1
        return count