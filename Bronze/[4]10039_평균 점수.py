# 기말고사 점수가 40점 이상인 학생들은 그 점수 그대로 자신의 성적이 된다. 하지만, 40점 미만인 학생들은 보충학습을 듣는 조건을 수락하면 40점을 받게 된다
# 학생 5명의 점수가 주어졌을 때, 평균 점수를 구하는 프로그램을 작성하시오.

import sys

total_score = 0

for i in range(5):
    a =  int(sys.stdin.readline())
    if a < 40:
        total_score += 40
    else:
        total_score += a

print(total_score // 5)