class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import Counter
        ans = []
        for i in range(len(nums)-k+1):
            check = nums[i:i+k]
            freq = Counter(check)
            top = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)[:x] 
            ans.append(sum(val * count for val, count in top))
        return ans