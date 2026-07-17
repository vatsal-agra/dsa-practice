class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the meeting point inside the cycle
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]          # Move one step
            fast = nums[nums[fast]]    # Move two steps

            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle
        ptr1 = 0
        ptr2 = slow    # or fast, both are at the meeting point

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1