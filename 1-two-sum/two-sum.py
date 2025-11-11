class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], index]
            else:
                store[num] = index    

        #store the items in a hashmap.
        #loop array using enumerate
            #set diff as target - array item
            #if the target is in the hashmap return the index's of both
            #if it is not then add that item to the hashmap