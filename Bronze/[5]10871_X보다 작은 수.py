# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

n, x = map(int, input().split())
sequence = list(map(int, input().split()))
result = []

for num in sequence:
    if num < x :
        result.append(num)

answer = " ".join(map(str, result))
print(answer) # 리스트의 요소를 문자로 결합하여 출력
print(*result) # 리스트나 튜플의 요소들을 개별적으로 함수의 인자로 전달