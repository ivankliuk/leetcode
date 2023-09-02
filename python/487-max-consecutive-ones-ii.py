from typing import List

"""
487. Max Consecutive Ones II
============================
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.


Example 1:
----------
Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Example 2:
----------
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.

Constraints:
------------
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


class Solution:
    """
    Algorithm
    ---------
    Two pointers approach.
    Left and right pointers start from 0 and move to the left.
    Right pointer moves if:
        - current element is 1;
        - current element is 0 and current number of allowed zeros is not equal to 1.

    Otherwise, left pointer moves if:
        - current element is 1 move left pointer;
        - current element is 0 move left pointer and decrement number of allowed zeros.

    Check longest sequence at each iteration step.

    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(1)
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_seq = 0
        l = r = 0
        num_zeroes = 0

        while r <= len(nums) - 1:
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0:
                if num_zeroes != 1:
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
