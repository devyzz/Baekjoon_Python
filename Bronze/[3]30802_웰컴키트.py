#티셔츠는 S, M, L, XL, XXL, 그리고 XXXL의 6가지 사이즈가 있습니다. 티셔츠는 같은 사이즈의 T장 묶음으로만 주문할 수 있습니다.
#펜은 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문할 수 있습니다.

# 총 N명의 참가자 중 S, M, L, XL, XXL, XXXL 사이즈의 티셔츠를 신청한 사람은 각각 S, M, L, XL, XXL, XXXL명입니다.
# 티셔츠는 남아도 되지만 부족해서는 안 되고 신청한 사이즈대로 나눠주어야 합니다. 펜은 남거나 부족해서는 안 되고 정확히 참가자 수만큼 준비되어야 합니다.
# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지, 그리고 펜을
# P자루씩 최대 몇 묶음 주문할 수 있고, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.

# 참가자 수 입력
participants = int(input())

# 각 아이템의 수량 입력
item_counts = list(map(int, input().split()))

# 티셔츠 묶음 크기와 펜 묶음 크기 입력
tshirt_bundle, pen_bundle = map(int, input().split())

# 티셔츠 묶음 수 계산
total_tshirts = 0
for count in item_counts:
    total_tshirts += (count + tshirt_bundle - 1) // tshirt_bundle  # ceil(count / tshirt_bundle)

# 펜 개수 계산
pens = participants // pen_bundle
pen_remainder = participants % pen_bundle

# 결과 출력
print(total_tshirts)
print(pens, pen_remainder)
