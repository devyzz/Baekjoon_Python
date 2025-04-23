# 창영이는 크로스워드 퍼즐을 만들려고 한다.
# 두 단어 A와 B가 주어진다. A는 가로로 놓여야 하고, B는 세로로 놓여야 한다. 또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다)
# 공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다.
# 마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다. 예를 들어, A = "ABBA"이고, B = "CCBB"라면, 아래와 같이 만들 수 있다.

A, B = input().split()
N = len(A)
M = len(B)
matrix = [['.'] * N for _ in range(M)]

for i in range(N):
    if A[i] in B:
        row = i
        col = B.index(A[i])
        break

for i in range(M):
    matrix[i][row] = B[i]
for i in range(N):
    matrix[col][i] = A[i]

for i in matrix:
    print(''.join(i))



