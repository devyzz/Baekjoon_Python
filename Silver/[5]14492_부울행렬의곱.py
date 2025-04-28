# 문제를 출제하던 욱제는 갑자기 괴랄한 문제를 내고 싶어졌다. 불행하게도, 이번 대회에는 프로그래밍 뉴비들이 많기 때문에 그럴 수는 없었다. 하지만 욱제는 신입생들을 괴롭히고픈 욕망을 포기할 수 없었다.
# ‘하하! 과연 신입생들이 이 문제를 풀 수 있을까?’
# 문제는 간단하다. N×N 크기의 두 부울행렬(0과 1로만 이루어진 행렬) A=[aij]와 B=[bij]가 주어졌을 때, 두 행렬에 대해 부울곱 연산을 수행한 행렬 C=[cij]에 나타나는 1의 개수를 세는 것이다. 부울곱 연산은 아래와 같이 수행된다.
# cij = (ai1∧b1j)∨(ai2∧b2j)∨...∨(ain∧bnj)
# xij는 X행렬의 i행j열 원소를 뜻하며 ∧는 논리곱(AND), ∨는 논리합(OR) 연산을 나타낸다. 자, 어서 코딩하자!

N = int(input())

# 행렬 A 입력
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B 입력
B = [list(map(int, input().split())) for _ in range(N)]

count = 0

# 부울곱 계산
for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i][k] and B[k][j]:
                count += 1
                break

print(count)
