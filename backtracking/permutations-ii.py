# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.freqs = Counter(nums)

        self.n = len(nums)
        self.permsList = []
        self.backtrack([])
        return self.permsList

    def backtrack(self, perm):
        if len(perm) == self.n:
            self.permsList.append(perm)
            return

        for n in self.freqs:
            if self.freqs[n]:
                self.freqs[n] -= 1
                self.backtrack(perm + [n])
                self.freqs[n] += 1

    # example: nums = [1,1,2]

    # backtrack([]) freqs = {1: 2, 2: 1}
        # backtrack([1]) freqs = {1: 1, 2: 1}
            # backtrack([1,1]) freqs = {1: 0, 2: 1}
                # backtrack([1,1,2]) freqs = {1: 0, 2: 0} -> added to permsList
            # backtrack([1,2]) freqs = {1: 1, 2: 0}
                # backtrack([1,2,1]) freqs = {1: 0, 2: 0} -> added to permsList
        # backtrack([2]) freqs = {1: 2, 2: 0}
            # backtrack([2,1]) freqs = {1: 1, 2: 0}
                # backtrack([2,1,1]) freqs = {1: 0, 2: 0} -> added to permsList
