# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

N = int(input())
answer = [int(sys.stdin.readline().strip()) for _ in range(N)]

answer.sort()
tmp = ''
for num in answer:
    if tmp != num:
        tmp = num
        print(num)