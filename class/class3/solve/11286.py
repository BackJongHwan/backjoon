import sys
input = sys.stdin.readline
class Heap:
    def __init__(self):
        self.heap = []
    def _parent(self, index):
        return (index - 1) // 2
    def _left_child(self, index):
        return index * 2 + 1
    def _right_child(self, index):
        return index * 2 + 2
    def _has_left_child(self, index):
        return self._left_child(index)  < len(self.heap)
    def _has_right_child(self, index):
        return self._right_child(index) < len(self.heap)
    def _has_parent(self, index):
        return self._parent(index) >= 0
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    def empty(self):
        return self.size() == 0
    def size(self):
        return len(self.heap)
    def _peek(self):
        return self.heap[0]
    def insert(self, value):
        self.heap.append(value)
        self._heap_up(len(self.heap) - 1)
    def pop(self):
        if self.empty():
            return 0
        value = self._peek()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heap_down(0)
        return value
    def _heap_up(self,index):
        while self._has_parent(index):
            parent_index = self._parent(index)
            if self._compare(self.heap[index], self.heap[parent_index]):
                self._swap(parent_index, index)
                index = parent_index 
            else:
                break
    def _heap_down(self, index):
        while self._has_left_child(index):
            smaller_child_index = self._left_child(index)
            if self._has_right_child(index):
                right_child_index = self._right_child(index)
                if self._compare(self.heap[right_child_index], self.heap[smaller_child_index]):
                    smaller_child_index = right_child_index
            if self._compare(self.heap[smaller_child_index], self.heap[index]):
                self._swap(smaller_child_index, index)
                index = smaller_child_index
            else:
                break
    ''' 
    If return true, then value1 is for change
    '''
    def _compare(self, value1, value2):
        abs1, abs2 = abs(value1), abs(value2)
        if abs1 == abs2:
            return value1 < value2
        else:
            return abs1 < abs2

n = int(input())
heap = Heap()
for _ in range(n):
    x = int(input())
    if(x == 0):
        value = heap.pop()
        print(value)
    else:
        heap.insert(x)
'''using libarary
import heapq
import sys
input = sys.stdin.readline

class AbsHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        # (절댓값, 원래값)을 튜플로 저장
        heapq.heappush(self.heap, (abs(value), value))
    
    def pop(self):
        if not self.heap:
            return 0
        # 튜플의 두 번째 값(원래값)을 반환
        return heapq.heappop(self.heap)[1]
    
    def size(self):
        return len(self.heap)

n = int(input())
heap = AbsHeap()
for _ in range(n):
    x = int(input())
    if x == 0:
        value = heap.pop()
        print(value)
    else:
        heap.insert(x)
'''