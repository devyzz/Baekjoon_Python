# 아프가니스탄의 아름다운 도시 중 한 곳에서 두 자매가 수학 숙제를 풀기 위해 간단한 게임을 프로그래밍하려고 합니다. 숙제는 두 수의 합과 곱을 계산하는 것입니다.
# 여러분의 과제는 자매가 숙제를 위한 간단한 프로그램을 만들도록 돕는 것입니다.


import sys

T  = int(input())

for i in range(T):
    N = int(input())
    for j in range(N):
        a, b = map(int, input().split())
        print(a+b, a*b)
