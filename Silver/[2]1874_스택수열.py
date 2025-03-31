# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
import sys

N = int(input())
targets = [sys.stdin.readline().strip() for _ in range(N)]
stack = []
answer = []
last_number = 1
is_possible = True

for target in targets:
    while is_possible:
        if not stack:
            stack.append(last_number)
            answer.append('+')
            last_number += 1
        else:
            if int(target) == stack[-1]:
                stack.pop()
                answer.append('-')
                break
            elif int(target) in stack and int(target) > stack[-1]:
                while int(target) != stack[-1]:
                    stack.pop()
                    answer.append('-')
                stack.pop()
                answer.append('-')
                break
            elif int(target) not in stack and int(target) >= last_number:
                while int(target) != stack[-1]:
                    stack.append(last_number)
                    last_number += 1
                    answer.append('+')
                stack.pop()
                answer.append('-')
                break
            else:
                is_possible = False

if is_possible:
    for ans in answer:
        print(ans)
else:
    print("NO")
