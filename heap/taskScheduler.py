# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/
# The approach we took in this problem was to use a frequency table to keep track of the 
# letters (tasks) that are remaining, and a heap that for each letter tracks the smallest
# step (or CPU cycle) that the letter can be used.
# At each step, we pop from the heap and reinsert the letter if its frequency is above 0.
# We reinsert it with a new step currentStep + n, where n is the cooldown for each task.
class StepNode:
    def __init__(self, letter, step, freq):
        self.letter = letter
        self.step = step # least index you're allowed to use it
        self.freq = freq
        
    def __lt__(self, other):
        return self.step < other.step or (self.step == other.step and self.freq > other.freq)
    
    def __repr__(self):
        return f"({self.letter}, {self.step}, {self.freq})"


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_table = Counter(tasks)
        freq_heap = [(-v, k) for k, v in freq_table.items()]
        heapify(freq_heap) 
        
        l = []
        for i in range(len(freq_heap)):
            result = heappop(freq_heap)
            heappush(l, StepNode(result[1], i, abs(result[0])))
        # [A,0,3]
        #   v
        # [B,1,3]
        i = 0
        while l:
            peek = l[0]
            if peek.step < i:
                node = heappop(l)
                node.step += 1
                heappush(l, node)
                continue
                
            if peek.step > i:
                i += 1
                continue
            i += 1
                
            node = heappop(l)
            node.freq -= 1
            if node.freq > 0:
                node.step += n + 1
                heappush(l, node)
            
        return i

