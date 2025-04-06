# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

import sys

n, m = map(int, input().split())
sentences = []
answer = 0

for _ in range(n):
    sentence = sys.stdin.readline()
    sentences.append(sentence)

for _ in range(m):
    target = sys.stdin.readline()
    if target in sentences:
        answer += 1

print(answer)