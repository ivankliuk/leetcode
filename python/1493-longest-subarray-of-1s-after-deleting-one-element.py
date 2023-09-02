from typing import List

"""
1493. Longest Subarray of 1's After Deleting One Element
========================================================
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
----------
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
----------
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
----------
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 
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
        - current element is 0 and has_zero flag is set.

    Otherwise, left pointer moves if:
        - current element is 1 move left pointer;
        - current element is 0 move left pointer and set has_zero flag.

    Check longest sequence at each iteration step.

    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(1)
    """

    def longestSubarray(self, nums: List[int]) -> int:
        longest_seq = i = j = 0
        has_zero = False

        while j <= len(nums) - 1:
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0:
                if not has_zero:
                    has_zero = True
                    j += 1
                else:
                    if nums[i] == 0:
                        has_zero = False
                        i += 1
                    else:
                        i += 1

            longest_seq = max(longest_seq, j - i)

        return longest_seq - 1
