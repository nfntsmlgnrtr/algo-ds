# 410. Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# This is essentially just the brute force algorithm we came up with,
# but transformed into top-down DP. The key two changes were passing
# a starting index (rather than an array) as parameter, and precomputing
# the array of prefix sums at the beginning rather than (re)computing
# the sums in the calls themselves.

from functools import lru_cache
from itertools import accumulate

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        prefix_sum = [0] + list(accumulate(nums))
        
        @lru_cache(None)
        def helper(i, mm):
            if mm == 1:
                return prefix_sum[n] - prefix_sum[i]
            
            best = prefix_sum[n]
            for j in range(i, n-mm+1):
                current_chunk_sum = prefix_sum[j+1] - prefix_sum[i]
                
                current_obj_val = max(current_chunk_sum, helper(j+1, mm-1))
                best = min(best, current_obj_val)
                
                if current_chunk_sum >= best:
                    break
            
            return best
        
        return helper(0, m)