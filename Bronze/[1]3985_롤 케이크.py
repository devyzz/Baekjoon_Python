# 인기 티비 프로그램 "나는 요리사 인가?"의 새 시즌이 시작한다. 이번 시즌은 기네스북에 등재될 만한 음식을 만드는 것을 목표로 진행한다.
# 첫 번째 에피소드에 출연하는 요리사는 전설의 요리사 김상근이고, 길이 L미터의 롤 케이크를 만들 것이다.
# 상근은 몇 시간동안 집중해서 케이크를 만들었고, 이제 스튜디오의 방청객 N명에게 케이크를 나누어 주려고 한다.
# 상근이는 롤 케이크를 펼쳐서 1미터 단위로 잘라 놓았다. 가장 왼쪽 조각이 1번, 오른쪽 조각이 L번 조각이다.
# 방청객은 1번부터 N번까지 번호가 매겨져 있다. 각 방청객은 종이에 자신이 원하는 조각을 적어서 낸다.
# 이때, 두 수 P와 K를 적어서 내며, P번 조각부터 K번 조각을 원한다는 뜻이다.

# 가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호와 실제로 가장 많은 케이크 조각을 받는 방청객의 번호를 구하는 프로그램을 작성하시오.
import sys

L = int(input())
M = int(input())
requests = [sys.stdin.readline().strip() for _ in range(M)]
cake = [0]*L
expects = 0
reals = 0

diff = 0
real_diff = 0
for i, se in enumerate(requests):
    s,e = map(int,se.split(' '))

    # 가장 많이 받을 것으로 예상되던 방청객
    if e-s > diff:
        expects = i+1
        diff = e-s
    # 실제로 가장 많이 받은 방청객
    for num in range(s,e+1):
        if cake[num-1] == 0:
            cake[num-1] = i+1

    if cake.count(i+1) > real_diff:
        reals = i+1
        real_diff = cake.count(i+1)

print(expects)
print(reals)
