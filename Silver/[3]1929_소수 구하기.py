# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
import math

M, N = map(int, input().split())

for i in range(M, N + 1):
    if i < 2:  # 1은 소수가 아니므로 건너뜀
        continue

    flag = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = False
            break

    if flag:
        print(i)



