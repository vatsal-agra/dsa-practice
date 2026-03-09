class Solution(object):
    def pivotInteger(self, n):

        for i in range(1, n+1):

            left = i*(i+1)//2
            right = (n*(n+1)//2) - ((i-1)*i//2)

            if left == right:
                return i

        return -1