import sys
# 메모리초과
N = int(input())
numbers = []
for i in range(N):
    numbers.append(sys.stdin.readline().strip())

numbers.sort()
print('\n'.join(map(str, numbers)))

# 정답
N = int(input())
count = [0] * 10001

for _ in range(N):
    number = int(sys.stdin.readline())
    count[number] += 1

output = []
for i in range(1, 10001):
    if count[i] > 0:
        for j in range(count[i]):
            print(i)
