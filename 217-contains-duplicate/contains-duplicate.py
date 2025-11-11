class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        store = {}

        for i, n in enumerate(nums):
            if n in store:
                return True                
            else:
                store[n] = i
        return False        
         

        #create a hashmap to store in numbers
            #loop and add each item to the hashmap
                #if already in the hashmap
                    #return true
                #if the loop ends
                    #return false    