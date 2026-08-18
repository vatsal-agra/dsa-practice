class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        window = [0]*len(code)
        check = len(code)
        if k>0:
            for i in range(len(code)):
                counter = i+1
                while counter <= i+k:
                    #print(counter, i ,k)
                    window[i] += code[counter % check]
                    counter += 1
                    #print(window)
            return window
        elif k<0:
            for i in range(len(code)):
                counter = i-1
                while counter >= i+k:
                    #print(counter, i ,k)
                    window[i] += code[counter % check]
                    counter -= 1
                    #print(window)
            return window
        else:
            return window