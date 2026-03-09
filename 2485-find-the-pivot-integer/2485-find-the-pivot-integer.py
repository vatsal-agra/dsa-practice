class Solution(object):
    def pivotInteger(self, n):

        prefix = [0]*(n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + i

        total = prefix[n]

        for i in range(1, n+1):
            left = prefix[i]
            right = total - prefix[i-1]

            if left == right:
                return i

        return -1