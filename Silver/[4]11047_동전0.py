# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
answer = 0

for coin in reversed(coins):
    if k >= coin:
        answer += k // coin
        k = k % coin

print(answer)
