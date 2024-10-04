from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize two pointers: 
        # 'actual_Index' to track the position to insert unique elements,
        # and 'current_Index' to iterate through the 'nums' list.
        actual_Index = current_Index = 0
        n = len(nums)  # Get the length of the input list

        # Loop until we reach the end of the list
        while current_Index < n:
            # Assign the current element to the 'actual_Index' position
            nums[actual_Index] = nums[current_Index]
            actual_Index += 1  # Move to the next position for the next unique element

            # Move to the next different element in the list
            next_Index = current_Index + 1
            while next_Index < n and nums[next_Index] == nums[current_Index]:
                next_Index += 1  # Skip duplicates

            # Update 'current_Index' to the next different element's index
            current_Index = next_Index

        # Return the number of unique elements found
        return actual_Index

# Time Complexity:
# The outer while loop iterates through all elements of the list, making the time complexity O(n),
# where 'n' is the number of elements in 'nums'. The inner loop skips over duplicates, 
# so each element is processed at most once.

# Space Complexity:
# This algorithm uses only a few extra variables for indexing, so the space complexity is O(1) (constant space),
# as it modifies the input list in place without using additional data structures.