class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        while len(stones)>1:
            stones.sort()
            x = stones[-2]
            y = stones[-1]
            if x == y:
                stones.remove(y)
                stones.remove(y)
            else:
                stones.remove(x)
                stones[-1] = y-x

        return stones[0] if len(stones) == 1 else 0