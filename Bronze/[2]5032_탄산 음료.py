# 준민이는 탄산 음료를 좋아한다. 탄산 음료를 사느라 돈을 다 써버렸기 때문에, 이제 준민이는 가진 돈이 없어 탄산 음료를 사먹을 수 없다.
# 준민이는 항상 법을 지키며 사는 사람이기 때문에, 아무리 탄산 음료가 먹고 싶어도 훔치지 않는다. 따라서, 법적으로 문제가 없는 방법으로 탄산 음료를 구매할 것이다.
# 마침 빈 병을 특정 개수만큼 가져가면, 새 병으로 바꾸어주는 이벤트가 진행중이다. 준민이는 길에서 빈 병을 열심히 찾은 뒤, 탄산 음료를 먹으려고 한다.
# 준민이가 현재 가지고 있는 빈 병의 수와 길에서 발견한 빈 병의 수, 새 병으로 바꾸는데 필요한 빈 병의 수가 주어졌을 때, 준민이가 탄산 음료를 몇 개 먹을 수 있는지 구하는 프로그램을 작성하시오.

e, f, c = map(int, input().split())
total = e + f
answer = 0

while total >= c:
    new = total // c
    answer += new
    total = new + (total % c)

print(answer)




