# 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.
# 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.

# 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
# 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.
import sys

N = int(input())
people = []
for i in range(N):
    weight, height = map(int, sys.stdin.readline().strip().split(' '))
    people.append((weight,height))

ranks = []

for i in range(N):
    cnt = 0
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt +=1
    ranks.append(cnt+1)

for rank in ranks:
    print(rank, end=" ")