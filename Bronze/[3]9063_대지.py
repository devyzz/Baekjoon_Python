# 첫째 줄에는 점의 개수 N (1 ≤ N ≤ 100,000) 이 주어진다.
# 이어지는 N 줄에는 각 점의 좌표가 두 개의 정수로 한 줄에 하나씩 주어진다. 각각의 좌표는 -10,000 이상 10,000 이하의 정수이다.

# 첫째 줄에 N 개의 점을 둘러싸는 최소 크기의 직사각형의 넓이를 출력하시오.
import sys

N = int(input())

x = []
y = []

for i in range(N):
    dots = sys.stdin.readline().rstrip()
    a,b = map(int, dots.split())
    x.append(a)
    y.append(b)

xval = max(x) - min(x)
yval = max(y) - min(y)

answer = xval * yval
print(answer)
