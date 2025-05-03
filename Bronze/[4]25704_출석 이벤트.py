# 쇼핑몰에서 30일간 출석 이벤트를 진행한다. 쇼핑몰의 사이트를 방문하면 1일 1회 출석 도장을 받을 수 있고, 출석 도장을 여러 개 모아서 할인 쿠폰으로 교환할 수 있다.
#
# 출석 도장의 개수에 따라 교환할 수 있는 할인 쿠폰의 종류가 달라진다.
#
# 출석 도장 5개   → 500원 할인 쿠폰
# 출석 도장 10개 → 10% 할인 쿠폰
# 출석 도장 15개 → 2,000원 할인 쿠폰
# 출석 도장 20개 → 25% 할인 쿠폰
# 경태가 모은 출석 도장의 개수와 구매할 물건의 가격이 주어졌을 때, 경태가 지불해야 하는 최소 금액을 구하시오. 단, 할인 쿠폰은 최대 하나만 적용 가능하다. 할인 금액이 물건의 가격보다 더 큰 경우 지불해야 하는 금액은 0원이다.

def calculate_final_price(N, P):
    discounts = [0]  # 할인 금액 목록 초기화

    if N >= 5:
        discounts.append(500)
    if N >= 10:
        discounts.append(P // 10)  # 10% 할인
    if N >= 15:
        discounts.append(2000)
    if N >= 20:
        discounts.append(P // 4)  # 25% 할인

    max_discount = max(discounts)
    final_price = P - max_discount

    return max(final_price, 0)  # 결제 금액은 0원 이상이어야 함

# 입력 받기
N = int(input())
P = int(input())

# 결과 출력
print(calculate_final_price(N, P))
