class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
                
         return len(set(nums)) != len(nums)

        #put nums into a set and see if the lengths are the same
        #set will eliminate duplicates so if any duplicates it'll remove them
        #therefore the lengths will be diffferent   