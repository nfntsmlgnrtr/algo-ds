# 895. Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
class FreqStack:

    def __init__(self):
        # Array of stacks
        self._stacks = [] # who is closest to the top out of all the top frequencies
        self._index_table = {} # top frequencies (calls * O(n))
        
        # Array of stacks
        # []
        # i = 0 => first index maps to frequency 1
        # push 1,2,3 => [[1,2,3]]
        # push 1     => [[1,2,3], [1]]
        # push 2     => [[1,2,3], [1, 2]] 
        # pop        => [[1,2,3], [1]] => 2

    def push(self, val: int) -> None:
        index = self._index_table.get(val, -1) + 1
        self._index_table[val] = index
        
        if len(self._stacks) - 1 < index:
            self._stacks.append([]) 
        
        self._stacks[index].append(val)

    def pop(self) -> int:
        val = self._stacks[-1].pop()
        if not self._stacks[-1]: 
            self._stacks.pop()
            
        self._index_table[val] -= 1
        return val
    
    # push 5 => [[5]]
    # push 7 => [[5,7]]
    # push 5 => [[5,7], [5]]
    # push 7 => [[5,7], [5,7]]
    # push 4 => [[5,7,4], [5,7]]
    # push 5 => [[5,7,4], [5,7], [5]]
    # pop => [[5,7,4], [5,7]] => 5
    # pop => [[5,7,4], [5]] => 7
    # pop => [[5,7,4]] => 5
    # pop => [[5,7]] => 4

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
