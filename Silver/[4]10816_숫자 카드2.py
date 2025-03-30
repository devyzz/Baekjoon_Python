# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오
# import sys

import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
cards = sys.stdin.readline().split()

M = int(sys.stdin.readline().strip())
targets = sys.stdin.readline().split()

# cards에서 각 숫자의 개수를 셈
count_dict = Counter(cards)

answer = []

for target in targets:
    cnt = str(count_dict[target])  # target의 개수를 가져옴, 없으면 0
    answer.append(cnt)  # 개수를 answer에 추가

print(' '.join(answer))  # 결과 출력