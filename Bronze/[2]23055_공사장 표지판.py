# 첫째 줄에 정수 N이 주어진다.
# N x N 크기의 출입제한 표지판을 출력한다.

N = int(input())

for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1:  # 첫 번째 행, 마지막 행
            print("*", end="")
        elif j == 0 or j == N - 1:  # 첫 번째 열, 마지막 열
            print("*", end="")
        elif i == j or i == N - j - 1:  # 대각선 조건
            print("*", end="")
        else:
            print(" ", end="")
    print()  # 줄바꿈

