#n=10^5 -> O(nlogn)
#using list
'''
import sys
# from collections import deque
input = sys.stdin.readline

def min_heap(n, heap):
    if(n == 0):
        # print(heap)
        if(len(heap) == 1):
            print(0)
        else:
            l = len(heap) - 1
            value = heap[1]
            heap[1] = heap[l]
            heap.pop()
            l -= 1
            idx = 1
            while 2 * idx <= l:
                left = 2 * idx
                right = 2 * idx + 1
                smallest = idx

                if left <= l and heap[left] < heap[smallest]:
                    smallest = left
                if right <= l and heap[right] < heap[smallest]:
                    smallest = right

                if smallest != idx:
                    heap[idx], heap[smallest] = heap[smallest], heap[idx]
                    idx = smallest
                else:
                    break
            print(value)
    else:
        heap.append(n)
        l = len(heap) - 1
        while (l > 1 and heap[l] < heap[l // 2] ):
            heap[l] , heap[l // 2] = heap[l//2] , heap[l]
            l = l // 2

n = int(input())
heap = [0]
for _ in range(n):
    x = int(input())
    min_heap(x, heap)
'''
#using module
import sys
input = sys.stdin.readline
import heapq
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if(x == 0):
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)