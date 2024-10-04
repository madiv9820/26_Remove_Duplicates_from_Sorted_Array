from typing import List
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Create a Counter object to count occurrences of each element in 'nums'
        # Then, extract only the unique elements by getting the dictionary keys
        # Counter retains the order of first occurrence, so the original order is preserved.
        unique_Values = list(Counter(nums).keys())
        
        # Replace the first part of 'nums' with the unique values
        for index in range(len(unique_Values)):
            nums[index] = unique_Values[index]
        
        # Return the number of unique elements, which is the length of 'unique_Values'
        return len(unique_Values)

# Time Complexity:
# 1. Counting the occurrences using Counter(nums) takes O(n), where 'n' is the number of elements in 'nums'.
# 2. Extracting the keys and iterating over unique values both take O(k), where 'k' is the number of unique elements.
# Since the number of unique elements 'k' is at most 'n', the overall time complexity is O(n).

# Space Complexity:
# 1. Counter(nums) stores a dictionary of size O(k), where 'k' is the number of unique elements.
# 2. The list of unique elements also takes O(k) space.
# Thus, the space complexity is O(k), where 'k' is the number of unique elements in 'nums'.