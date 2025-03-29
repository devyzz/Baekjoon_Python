# 아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
# 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.
# 사용자들이 어떤 문제에 제출한 난이도 의견 목록이 주어질 때, solved.ac가 결정한 문제의 난이도를 계산하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

def round2(num):  # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

# 입력
n = int(input())
ban = round2(n * 0.15)

if n == 0:
    print(0)
else:
    score = []
    for _ in range(n):
        score.append(int(input()))
    score.sort()

    # 출력
    res = 0
    for i in range(ban, n - ban):
        res += score[i]
    res = res / (n - 2 * ban)
    print(round2(res))