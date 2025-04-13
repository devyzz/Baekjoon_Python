# 이진트리를 다음의 규칙에 따라 행과 열에 번호가 붙어있는 격자 모양의 틀 속에 그리려고 한다. 이때 다음의 규칙에 따라 그리려고 한다.

# 이진트리에서 같은 레벨(level)에 있는 노드는 같은 행에 위치한다.
# 한 열에는 한 노드만 존재한다.
# 임의의 노드의 왼쪽 부트리(left subtree)에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치하고, 오른쪽 부트리(right subtree)에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치한다.
# 노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.
# 이와 같은 규칙에 따라 이진트리를 그릴 때 각 레벨의 너비는 그 레벨에 할당된 노드 중 가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다.
# 트리의 레벨은 가장 위쪽에 있는 루트 노드가 1이고 아래로 1씩 증가한다.

# 첫째 줄에 노드의 개수를 나타내는 정수 N(1 ≤ N ≤ 10,000)이 주어진다.
# 다음 N개의 줄에는 각 줄마다 노드 번호와 해당 노드의 왼쪽 자식 노드와 오른쪽 자식 노드의 번호가 순서대로 주어진다.
# 노드들의 번호는 1부터 N까지이며, 자식이 없는 경우에는 자식 노드의 번호에 -1이 주어진다.

# 첫째 줄에 너비가 가장 넓은 레벨과 그 레벨의 너비를 순서대로 출력한다.
# 너비가 가장 넓은 레벨이 두 개 이상 있을 때에는 번호가 작은 레벨을 출력한다.

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
tree = {}
parent = {}
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a] = (b, c)
    parent[b] = a
    parent[c] = a

# 루트 노드 찾기
root = None
for i in range(1, n + 1):
    if i not in parent:
        root = i
        break

# 중위 순회하면서 열 위치 기록
x = 1
level_min = {}
level_max = {}
position = {}


def inorder(node, depth):
    global x
    if node == -1:
        return
    left, right = tree[node]
    inorder(left, depth + 1)

    position[node] = x
    level_min[depth] = min(level_min.get(depth, x), x)
    level_max[depth] = max(level_max.get(depth, x), x)
    x += 1

    inorder(right, depth + 1)


inorder(root, 1)

max_width = 0
level = 0
for d in level_min:
    width = level_max[d] - level_min[d] + 1
    if width > max_width:
        max_width = width
        level = d - 1

print(level, max_width)


