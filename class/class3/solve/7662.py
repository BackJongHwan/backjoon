#k = 10^6 -> O(n)
import sys
input = sys.stdin.readline
import heapq
class DualPriorityQueue:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.numDict = dict()
        self.size = 0
    def insert(self, value):
        if value in self.numDict:
            self.numDict[value] += 1
        else:
            self.numDict[value] = 1
        heapq.heappush(self.min_heap, value)
        heapq.heappush(self.max_heap, -value)
        self.size += 1
    def delete(self, cmd):
        if(not self.empty()):
        #max_value delete
            if(cmd == 1):        
                while self.numDict[-self.max_heap[0]] == 0:
                    heapq.heappop(self.max_heap)
                self.numDict[-heapq.heappop(self.max_heap)] -= 1
        #min_value delete
            else:
                while self.numDict[self.min_heap[0]] == 0:
                    heapq.heappop(self.min_heap)
                self.numDict[heapq.heappop(self.min_heap)] -= 1
            self.size -= 1
    def empty(self):
        return self.size == 0
    def max_value(self):
            while self.numDict[-self.max_heap[0]] == 0:
                heapq.heappop(self.max_heap)
            return -self.max_heap[0]
    def min_value(self):
            while self.numDict[self.min_heap[0]] == 0:
                heapq.heappop(self.min_heap)
            return self.min_heap[0]
test = int(input())
for _ in range(test):
    k = int(input())
    dualHeap = DualPriorityQueue()
    for _ in range(k):
        cmd1, cmd2 = input().split()
        cmd2 = int(cmd2)
        if(cmd1 == 'I'):
            dualHeap.insert(cmd2)
        else:
            if dualHeap.empty() == False:
                dualHeap.delete(cmd2)
    if(dualHeap.empty()):
        print("EMPTY")
    else:
        print(dualHeap.max_value(), dualHeap.min_value())