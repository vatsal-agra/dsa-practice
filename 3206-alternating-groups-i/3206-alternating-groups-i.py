class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        k = len(colors)
        for i in range(k):
            a=i
            b=i+3
            if b > k:
                b = b%k
                check = colors[a:] + colors[:b]
            else:
                check = colors[a:b]
            met = False
            for j in range(2):
                if check[j] == check[j+1]:
                    met = True
            if met == False:
                count += 1
        return count