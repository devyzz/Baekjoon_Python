# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(' ' + '* ' * n)
    else:
        print('* ' * n)

