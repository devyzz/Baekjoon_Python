#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline().strip())
target_set = set(sys.stdin.readline().strip().split(' '))

M = int(sys.stdin.readline().strip())
target_list = sys.stdin.readline().strip().split(' ')

for num in target_list:
    print(1 if num in target_set else 0)
