from collections import defaultdict
from heapq import *

# hash1(e1, freq): value->latest frequency
# hash2(freq, heap((pos1, e1), (pos2, e2), (pos3, e3))): freq -> val list with respective position when pushed
# heap - freq: frequency heap
# https://leetcode.com/problems/maximum-frequency-stack/
class FreqStack:
    # Constructor
    def __init__(self):
        self.heap = []
        self.val_freq_map = defaultdict(list)
        self.freq_val_map = defaultdict(list)

    def initialize(self):
        self.heap = []
        self.val_freq_map = defaultdict(list)
        self.freq_val_map = defaultdict(list)

    def push(self, val: int) -> None:
        if val in self.val_freq_map:
            new_freq = self.val_freq_map[val] + 1
        else:
            new_freq = 1
        self.val_freq_map[val] = new_freq

        if new_freq in self.freq_val_map:
            tmp_heap = self.freq_val_map[new_freq]
            new_pos = (len(self.heap)-1)
            lp, lv = tmp_heap[0]
            # due to pop, there maybe equal position, so just make pos larger if pushed later
            if new_pos <= abs(lp):
                new_pos = abs(lp) + 1
            heappush(tmp_heap, (-new_pos, val))
        else:
            tmp_heap = []
            heappush(tmp_heap, (-(len(self.heap)-1), val))
            self.freq_val_map[new_freq] = tmp_heap

        heappush(self.heap, -new_freq)

    def pop(self) -> int:
        if len(self.heap) == 0:
            return None

        freq = -heappop(self.heap)
        pos_heap = self.freq_val_map[freq]
        pos, val = heappop(pos_heap)
        if len(pos_heap) == 0:
            del self.freq_val_map[freq]

        self.val_freq_map[val] = self.val_freq_map[val] - 1
        if self.val_freq_map[val] == 0:
            del self.val_freq_map[val]

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
[[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
freqStack = FreqStack();
freqStack.push(4) # The stack is [5]
freqStack.push(0) # The stack is [5,7]
freqStack.push(9) # The stack is [5,7,5]
freqStack.push(3) # The stack is [5,7,5,7]
freqStack.push(4) # The stack is [5,7,5,7,4]
freqStack.push(2) # The stack is [5,7,5,7,4,5]
print(freqStack.pop())
freqStack.push(6)
print(freqStack.pop())
freqStack.push(1)
print(freqStack.pop())
freqStack.push(1)
print(freqStack.pop())
freqStack.push(4)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())