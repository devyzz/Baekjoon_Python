# 정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

import sys

S = sys.stdin.readline().rstrip()
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
target = int(sys.stdin.readline().rstrip())
is_target = False
s = 0
e = max(numbers)

for number in numbers:
    if number == target:
        is_target = True
    else:
        if number < target and s < number:
            s = number
        elif number > target and e > number:
            e = number

s = target - s
e = e - target
if is_target:
    print(0)
else:
    print(s*e-1)

