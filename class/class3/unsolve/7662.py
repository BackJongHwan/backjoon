#k = 10^6 -> O(n)
import sys
input = sys.stdin.readline
#binary Tree
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Btree:
    def __init__(self):
        self.root = None
        self.size = 0
    def empty(self):
        return self.size == 0
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
        self.size += 1
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert(current_node.right, value)
    def delete(self, cmd):
        if(cmd == 1):
            self.root = self._max_delete(self.root)
        else:
            self.root = self._min_delete(self.root)
        self.size -= 1
    def _max_delete(self, node):
        if node.right is None:
            return node.left
        node.right = self._max_delete(node.right)
        return node
    def _min_delete(self, node):
        if node.left is None:
            return node.right
        node.left = self._max_delete(node.left)
        return node
    def max_value(self):
        current_node = self.root
        while current_node.right != None:
            current_node = current_node.right
        return current_node.value
    def min_value(self):
        current_node = self.root
        while current_node.left != None:
            current_node = current_node.left
        return current_node.value
test = int(input())
for _ in range(test):
    k = int(input())
    bt = Btree()
    for _ in range(k):
        cmd, num = input().split()
        if cmd == 'I':
            num = int(num)
            bt.insert(num)
        else:
            if not bt.empty():
                if num == '1':
                    bt.delete(1)
                else:
                    bt.delete(-1)
    if bt.empty():
        print("EMPTY")
    else:
        print(bt.max_value(), bt.min_value())
'''

