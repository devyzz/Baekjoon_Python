# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
#첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

import sys

N, M = map(int, input().split())
boards = [sys.stdin.readline().strip() for _ in range(N)]

min_paint = 64

# 8x8 체스판을 만들 수 있는 모든 시작점을 탐색
for i in range(N - 7):
    for j in range(M - 7):
        paint_B = 0  # 'B'로 시작하는 경우
        paint_W = 0  # 'W'로 시작하는 경우

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:  # 체스판의 기준 패턴 (짝수 좌표)
                    if boards[x][y] != 'B':
                        paint_B += 1
                    if boards[x][y] != 'W':
                        paint_W += 1
                else:  # 체스판의 반대 패턴 (홀수 좌표)
                    if boards[x][y] != 'W':
                        paint_B += 1
                    if boards[x][y] != 'B':
                        paint_W += 1

        min_paint = min(min_paint, paint_B, paint_W)

print(min_paint)

