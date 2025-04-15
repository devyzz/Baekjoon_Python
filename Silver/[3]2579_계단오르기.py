# 계단 오르는 데는 다음과 같은 규칙이 있다.
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

'''
점화식
DP[i] = max(
    DP[i-2] + steps[i],                   # case 1
    DP[i-3] + steps[i-1] + steps[i]       # case 2
)
'''

import sys

n = int(sys.stdin.readline())
steps = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * n

if len(steps)<=2:
    print(sum(steps))
else:
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+steps[i-1]+steps[i], dp[i-2]+steps[i])
    print(dp[-1])



