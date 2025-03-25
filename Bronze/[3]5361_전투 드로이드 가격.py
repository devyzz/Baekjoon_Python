# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 음이 아닌 정수 다섯 개(A B C D E)로 이루어져 있다.

# A: 필요한 블래스터 라이플의 개수
# B: 필요한 시각 센서의 개수
# C: 필요한 청각 센서의 개수
# D: 필요한 팔의 수
# E: 필요한 다리의 수

## 각 테스트 케이스 마다, 입력으로 주어진 부품을 모두 구매하는데 필요한 비용을 소수점 둘째 자리까지 출력한다. 달러 표시도 출력해야 한다. 정답은 1억보다 작거나 같다.
import sys

N = int(input())  # 테스트 케이스 수 입력
prices = [350.34, 230.90, 190.55, 125.30, 180.90]
answer = ""

for i in range(N):
    amounts = list(map(int, sys.stdin.readline().split()))  # 각 상품의 수량 입력
    total_price = 0
    for idx in range(5):
        total_price += round(prices[idx] * amounts[idx], 2)  # 가격 계산
    answer += f"${total_price:.2f}\n"  # 결과 추가

print(answer)
