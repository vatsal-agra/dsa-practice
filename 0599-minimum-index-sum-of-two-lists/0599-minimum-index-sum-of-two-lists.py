class Solution(object):
    def findRestaurant(self, list1, list2):
        idx2 = {s: j for j, s in enumerate(list2)}   # string → its index in list2, built once
        least = float('inf')
        final = []
        for a, s in enumerate(list1):
            if s in idx2:                 # O(1) dict lookup, not a scan
                total = a + idx2[s]
                if total < least:
                    least = total
                    final = [s]
                elif total == least:
                    final.append(s)
        return final