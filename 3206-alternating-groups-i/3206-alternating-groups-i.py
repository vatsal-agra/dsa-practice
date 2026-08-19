class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        for i in range(len(colors)):
            a=i
            b=i+3
            if b > len(colors):
                b = b%len(colors)
                check = colors[a:] + colors[:b]
            else:
                check = colors[a:b]
           # print(check)
            met = False
            for i in range(2):
                #print("hi",check[i],check[i+1])
                if check[i] == check[i+1]:
                   # print("bye")
                    met = True
            if met == False:
                count += 1
              #  print("count", count)
        return count