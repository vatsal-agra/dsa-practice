class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        check = {}
        seen = False

        while not seen:
            a = n
            sum = 0
            while a>0:
                digit = a%10
                sum += digit*digit
                a = a // 10
            n = sum
            if sum == 1:
                return True
            if sum in check:
                seen = True
            else:
                check[sum] = 1
        return False