# tree search 

# make binary tree -> using dictionary
def preorder(tree, node, path):
    if(node == '.'):
        return
    path.append(node)
    preorder(tree, tree[node][0], path)
    preorder(tree, tree[node][1], path)

def inorder(tree, node, path):
    if(node == '.'):
        return
    inorder(tree, tree[node][0], path)
    path.append(node)
    inorder(tree, tree[node][1], path)
def postorder(tree, node, path):
    if(node == '.'):
        return
    postorder(tree, tree[node][0], path)
    postorder(tree, tree[node][1], path)
    path.append(node)
n = int(input())
tree = {}
for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)
pre_path = []
in_path = []
post_path = []
preorder(tree, 'A', pre_path)
inorder(tree, 'A',in_path)
postorder(tree, 'A', post_path)
print(''.join(pre_path))
print(''.join(in_path))
print(''.join(post_path))


