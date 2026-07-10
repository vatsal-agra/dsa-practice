class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        final = []
        least = float('inf')
        for i in list1:
            if i in list2:
                a=list1.index(i)
                b=list2.index(i)
                if abs(a+b)<least:
                    final[:] = []
                    final.append(i)
                    least = abs(a+b)
                elif abs(a+b)==least:
                    final.append(i)
        return final