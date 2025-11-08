class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_tracker = {}
        for i in nums:
            if i in num_tracker:
                return True
            num_tracker[i] = i

        return False
