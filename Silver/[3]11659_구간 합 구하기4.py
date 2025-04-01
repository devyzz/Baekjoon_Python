# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
import sys

N, M = map(int,sys.stdin.readline().rstrip().split(' '))
numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

for _ in range(N):
    s, e = map(int,sys.stdin.readline().rstrip().split(' '))
    print(sum(numbers[s-1:e]))