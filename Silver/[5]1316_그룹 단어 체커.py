# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
import sys

n = int(input())

words = [sys.stdin.readline().rstrip() for _ in range(n)]

answer = 0

for word in words:
    contain = []
    is_repeat = True
    for idx,char in enumerate(word):
        if idx == 0:
            contain.append(char)
        else:
            if char in contain:
               if contain[-1] != char:
                   is_repeat = False
            else:
                contain.append(char)
    if is_repeat:
        answer += 1

print(answer)



