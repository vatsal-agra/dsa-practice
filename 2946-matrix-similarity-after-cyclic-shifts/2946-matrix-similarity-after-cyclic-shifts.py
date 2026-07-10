class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        count = 0
        num = len(mat[0])
        check = []
        shift = k%num if k>=num else k
        if shift == 0:
            return True
        for i in mat:
            if count % 2 == 0:
                check.append(i[shift:]+i[:shift])
                
            else:
                check.append(i[num-shift:]+i[:num-shift])
                
            count += 1
       
        if check == mat:
            return True
        return False