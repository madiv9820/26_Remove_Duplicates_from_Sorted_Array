# 26. Remove Duplicates from Sorted Array

__Type:__ Easy <br>
__Topics:__ Array, Two Pointers <br>
__Companies:__ Google, Bloomberg, Microsoft, Meta, Amazon, Apple, Adobe, Yahoo, Uber, tcs, Wipro, Infosys, Oracle, Flipkart, Accenture, Capgemini <br>
__LeetCode Link:__ [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
<hr>

### Question

Given an integer array `nums` sorted in __non-decreasing order__, remove the duplicates [__in-place__](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only once. The __relative order__ of the elements should be kept the __same__. Then return _the number of unique elements in_ `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in nums initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

__Custom Judge:__

The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be __accepted__.
<hr>

### Examples 

__Example 1:__

__Input:__ nums = [1,1,2] <br>
__Output:__ 2, nums = [1,2,_] <br>
__Explanation:__ Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.<br>
It does not matter what you leave beyond the returned k (hence they are underscores).

__Example 2:__

__Input:__ nums = [0,0,1,1,1,2,2,3,3,4] <br>
__Output:__ 5, nums = [0,1,2,3,4,_,_,_,_,_] <br>
__Explanation:__ Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores).
<hr>

### Constraints:

- <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>
- `-100 <= nums[i] <= 100`
- `nums` is sorted in __non-decreasing__ order.
<hr>

### Hints
- In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned, what is their positioning in the array when the given array is sorted? Look at the image below for the answer. If we know the position of one of the elements, do we also know the positioning of all the duplicate elements?
![](https://assets.leetcode.com/uploads/2019/10/20/hint_rem_dup.png)

- We need to modify the array in-place and the size of the final array would potentially be smaller than the size of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.

- Essentially, once an element is encountered, you simply need to bypass its duplicates and move on to the next unique element.