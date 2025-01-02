import sys
sys.setrecursionlimit(10**6)  
class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

data = []
for line in sys.stdin:
    data.append(int(line.strip()))  # 줄 단위로 입력받아 리스트에 추가
root = Tree(data[0])
def build_tree():
    root = Tree(data[0])
    stack = [root]
    for value in data[1:]:
        node = Tree(value)
        if value < stack[-1].value:
            stack[-1].left = node
        else:
            while stack and stack[-1].value < value:
                last = stack.pop()
            last.right = node
        stack.append(node)
    return root
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)
root = build_tree()
postorder(root)