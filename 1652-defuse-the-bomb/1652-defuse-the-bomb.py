class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        check = len(code)
        window = [0]*check
        
        if k>0:
            for i in range(check):
                counter = i+1
                while counter <= i+k:
                    window[i] += code[counter % check]
                    counter += 1
            return window
        elif k<0:
            for i in range(check):
                counter = i-1
                while counter >= i+k:
                    window[i] += code[counter % check]
                    counter -= 1
            return window
        else:
            return window