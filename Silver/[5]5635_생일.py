# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
infos = []
for _ in range(n):
    infos.append(input().rstrip().split())

sorted_infos = sorted(infos, key=lambda x:(int(x[3]), int(x[2]), int(x[1])))

print(sorted_infos[n-1][0])
print(sorted_infos[0][0])
