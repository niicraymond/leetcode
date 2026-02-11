class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        n,m = len(nums1), len(nums2)
        total = n + m
        half = (total + 1)//2

        l,r = 0, n
        while l <= r:
            i = (l+r)//2
            j = half-i

            leftA = nums1[i-1] if i > 0 else float("-inf")
            rightA = nums1[i] if i < n else float("inf")
            leftB = nums2[j-1] if j > 0 else float("-inf")
            rightB = nums2[j] if j < m else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return max(leftA, leftB)
                return(max(leftA,leftB)+min(rightA,rightB))/2

            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1    

                        
