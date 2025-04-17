# BIG 프로젝트로 동문 커뮤니티 웹사이트를 만들려고 한다. 동문 커뮤니티의 관리자는 홈페이지와 선후배 네트워크를 담당하는 일을 한다.
# 동문 커뮤니티 제작 프로젝트를 맡으신 Mr.Nam 교수님은 동문 커뮤니티 운영을 맡을 중요한 관리자를 뽑아달라는 부탁을 동아리에 전달했다.
#
# 회의 결과 다음과 같은 규칙으로 매년 각 동아리에서 관리자를 선출하자는 의견이 나왔다.
#
# 각 동아리에서는 동아리원 N명을 선출하여, 그 중 백준 온라인 저지 알고리즘 문제를 푼 개수가 가장 많은 사람을 그 동아리의 관리자 후보로 선출한다.
# 각 동아리에서 뽑힌 후보들 중 가장 문제를 많이 푼 후보가 최종적으로 관리자가 된다.
# 충남대학교 컴퓨터공학과는 다양한 분야의 동아리들이 활동하고 있다.
#
# 17년 기준으로 PROBRAIN, GROW, ARGOS, ADMIN, ANT, MOTION, SPG, COMON, ALMIGHTY 이렇게 총 9개의 동아리가 있고,
# 각 동아리에는 최소 N명의 동아리원이 있을 때, 동문 커뮤니티 관리자는 어느 동아리에서 선출 될 것인지 알아내어라.

import sys
input = sys.stdin.readline
circles = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

n = int(input())
max_score = 0
answer = ''
for circle in circles:
    scores = list(map(int,input().rstrip().split()))
    score = max(scores)
    if max_score < score:
        max_score = score
        answer = circle

print(answer)
