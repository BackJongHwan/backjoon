# N, M 1<= M, M <= 8, ascending order, no duplicate
# tree만들기 -> dfs이용
class Tree:
    def __init__(self, value = None):
        self.value = value
        self.children = []
def build_tree(nums, count, depth, max_depth):
    if depth == max_depth:  # 깊이에 도달하면 리프 노드 처리
        return None
    root = Tree()  # 현재 노드 생성
    for num in nums:
        if count[num] > 0:  # 사용 가능한 숫자만 처리
            count[num] -= 1
            child = Tree(num)  # 자식 노드 생성
            subtree = build_tree(nums, count, depth + 1, max_depth)  # 서브 트리 생성
            if subtree:  # 반환된 트리가 있다면 추가
                child.children.append(subtree)
            root.children.append(child)  # 현재 노드의 자식 리스트에 추가
            count[num] += 1  # 백트래킹
    return root

def dfs(tree, path, results):
    if tree.value is not None:  # 루트 노드 값은 None
        path.append(tree.value)
    if len(path) == m:  # M 길이의 수열 완성 시 결과 추가
        results.append(path[:])  # 깊은 복사
    else:
        for child in tree.children:  # 자식 노드를 탐색
            dfs(child, path, results)
    if tree.value is not None:  # 백트래킹
        path.pop()

def backtracking(k):
    if k == m:
        for i in range(m):
            print(answer[i], end = ' ')
        print()
        return
    temp = 0
    for i in range(n):
        if not checked[i] and temp != nums[i]:
            answer[k] = nums[i]
            checked[i] = True
            temp = nums[i]
            backtracking(k + 1)
            checked[i] = False
n, m =map(int, input().split())
nums = sorted(list(map(int, input().split())))
# counts = {num: nums.count(num) for num in nums}
# root = build_tree(nums, counts, 0, m)

# results =[]
# dfs(root, [], results)
# unique_results = sorted(set(tuple(result) for result in results))
# for result in unique_results:
#     print(' '.join(map(str, result)))
checked = [False] * n 
answer = [-1] * m
backtracking(0)