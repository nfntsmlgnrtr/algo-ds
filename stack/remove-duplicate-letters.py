# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = defaultdict(int)

        for x in s:
            remaining[x] += 1

        # could also just use collections.Counter for `remaining`

        stack = []

        # loop invariant: remaining[x] is the number of occurrences of x we have yet to process
        for x in s:
            if x in stack:
                remaining[x] -= 1
                continue

            while stack and remaining[stack[-1]] > 0 and stack[-1] > x:
                stack.pop()

            stack.append(x)
            remaining[x] -= 1

        return ''.join(stack)
