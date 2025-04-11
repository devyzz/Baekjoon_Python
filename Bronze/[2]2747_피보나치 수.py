# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

n = int(input())

f = [0] * (max(2, n + 1))
f[1] = 1

for i in range(2, n + 1):
    f[i] = f[i-1] + f[i-2]

print(f[n])

