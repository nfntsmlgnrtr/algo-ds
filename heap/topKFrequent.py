# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# We took 3 approaches: frequency table, building and popping a heap, and heapifying.
# One of the official solution uses the quickselect algorithm

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1
        # O(nlogn)
        # Frequency table -> sort()
        # key (number) -> [key, frequency]
        
        freq_table = {}
        for num in nums:
            freq = freq_table.get(num, 0)
            freq_table[num] = freq + 1
        
        unique_nums = []
        # sorted() -> takes in a dict
        # --> (num, freq), ... -> (num, freq) 
        freq_sorted = sorted(freq_table, key=freq_table.get, reverse=True)
        
        # [left, right)
        return freq_sorted[:k]
        # ulog(u), where u is the number of unique elements
        
        # Approach 2
        # heap
        # min-heap
        # 1,2,3,4,5,6,7,8,9,10
        # k = 3
        # (1)
        # (1,2)
        # (1,2,3) heap.size == 3
        # (2,3,4) heap.pop()
        # ...
        # (8,9,10)
        
        # Approach 3
        # you can heapify in linear time
        # create a list: [(freq, num), ...] size u, where u is the unique number of elements

        heapified_list = [(-v, k) for k, v in freq_table.items()] # list
        heapify(heapified_list)
        return [heappop(heapified_list)[1] for x in range(k)]\

            