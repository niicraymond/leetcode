class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letter_count_s = {}
        letter_count_t = {}

        for i in s:
            if i in letter_count_s:
                letter_count_s[i] += 1
            else:
                letter_count_s[i] = 1

        for j in t:
            if j in letter_count_t:
                letter_count_t[j] += 1
            else:
                letter_count_t[j] = 1  

        return letter_count_t == letter_count_s                  

        #create a hashmap to keep track of the letters and the occurences
        #loop string
            #if the letter is not in the hashmap add it and set val to 1
            #if it is then add 1 to its existing value

        #repeat this for the other string (maybe a helper function)
                #check for equality