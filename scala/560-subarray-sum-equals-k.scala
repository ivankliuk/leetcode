/*
560. Subarray Sum Equals K
==========================
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
----------
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
----------
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
------------
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
*/

object Solution {
    def subarraySum(nums: Array[Int], k: Int): Int = {
        /*
        Complexity Analysis
        -------------------
        Time complexity: O(n^2)
        Space complexity: O(n)
        */
        val prefixSum = Array.fill(nums.length + 1)(0)
        prefixSum(0) = 0

        var idx = 1
        while (idx <= nums.length) {
            prefixSum(idx) = prefixSum(idx - 1) + nums(idx - 1)
            idx += 1
        }

        var subArrays = 0
        for (i <- 0 to nums.length - 1) {
            for (j <- i to nums.length - 1) {
                if (prefixSum(j + 1) - prefixSum(i) == k) {
                    subArrays += 1
                }
            }
        }

        subArrays
    }
}
