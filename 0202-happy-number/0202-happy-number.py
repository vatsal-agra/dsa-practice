class Solution(object):
    def isHappy(self, n):
        def next_num(x):
            total = 0
            while x:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        slow = n
        fast = n

        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False