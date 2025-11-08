class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.track_letters(s) == self.track_letters(t)

    def track_letters(self, s: str) -> dict:
        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        return letters
