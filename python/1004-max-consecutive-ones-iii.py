"""
1004. Max Consecutive Ones III
==============================
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can
flip at most k 0's.

Example 1:
----------
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
----------
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:
------------
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List


class Solution:
    """
    Algorithm
    ---------
    Two pointers approach.
    Left and right pointers start from 0 and move to the left.
    Right pointer moves if:
        - current element is 1;
        - current element is 0 and current number of allowed zeros is not equal to k.

    Otherwise, left pointer moves if:
        - current element is 1 move left pointer;
        - current element is 0 move left pointer and decrement number of allowed zeros.

    Check longest sequence at each iteration step.

    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(1)
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        longest_seq = 0
        l = r = 0
        num_zeroes = 0
        allowed_nums_zeroes = k

        while r <= len(nums) - 1:
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0:
                if num_zeroes != allowed_nums_zeroes:
                    r += 1
                    num_zeroes += 1
                else:
                    if nums[l] == 1:
                        l += 1
                    if nums[l] == 0:
                        num_zeroes -= 1
                        l += 1

            longest_seq = max(longest_seq, r - l)

        return longest_seq
