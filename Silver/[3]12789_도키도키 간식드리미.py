# 입력의 첫째 줄에는 현재 승환이의 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)이 주어진다.
# 다음 줄에는 승환이 앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서가 앞에서부터 뒤 순서로 주어진다.
#
# 승환이가 무사히 간식을 받을 수 있으면 "Nice"(따옴표는 제외)를 출력하고 그렇지 않다면 "Sad"(따옴표는 제외)를 출력한다.

n = int(input())
students = list(map(int,input().split()))

stack = []
target = 1  # 간식 받을 번호

for student in students:
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    if student == target:
        target += 1
    else:
        stack.append(student)

# 남은 스택도 확인
while stack and stack[-1] == target:
    stack.pop()
    target += 1

print("Nice" if not stack else "Sad")