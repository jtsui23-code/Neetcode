from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # STEP 1: Make sure nums1 is the shorter array
        # This ensures our binary search is on the smaller array (more efficient)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # How many elements should be on the left side
        
        # STEP 2: Binary search on nums1
        left, right = 0, m
        
        while left <= right:
            # i = how many elements from nums1 are on the left side
            i = (left + right) // 2
            
            # j = how many elements from nums2 are on the left side
            # Since left side needs 'half' elements total: i + j = half
            j = half - i
            
            # STEP 3: Get the boundary elements around our partition
            # maxLeftA = largest element on left side of nums1
            # minRightA = smallest element on right side of nums1
            # (use -inf/inf for edge cases when partition is at the very start/end)
            
            maxLeftA = nums1[i - 1] if i > 0 else float('-inf')
            minRightA = nums1[i] if i < m else float('inf')
            
            maxLeftB = nums2[j - 1] if j > 0 else float('-inf')
            minRightB = nums2[j] if j < n else float('inf')
            
            # STEP 4: Check if we found the correct partition
            # A correct partition means:
            # - Everything on left ≤ everything on right
            # - maxLeftA ≤ minRightB (largest from A's left ≤ smallest from B's right)
            # - maxLeftB ≤ minRightA (largest from B's left ≤ smallest from A's right)
            
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # FOUND THE CORRECT PARTITION!
                
                # If total length is even, median is average of two middle elements
                if total % 2 == 0:
                    # The two middle elements are:
                    # - max of the left side (largest element on left)
                    # - min of the right side (smallest element on right)
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0
                else:
                    # If odd, median is the max of the left side
                    return max(maxLeftA, maxLeftB)
            
            # STEP 5: Adjust binary search based on which side needs correction
            elif maxLeftA > minRightB:
                # We took too many elements from nums1
                # Move partition to the LEFT (decrease i)
                right = i - 1
            else:
                # We took too few elements from nums1
                # Move partition to the RIGHT (increase i)
                left = i + 1
        
        return 0.0  # Should never reach here with valid input


