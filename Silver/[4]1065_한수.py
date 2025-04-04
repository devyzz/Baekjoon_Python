# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.


n = int(input())
answer = 0

for num in range(1, n + 1):
    if num < 100:
        answer += 1  # 1~99는 모두 한수
    else:
        digits = list(map(int, str(num)))
        diff = digits[1] - digits[0]
        is_hansu = True
        for i in range(1, len(digits) - 1):
            if digits[i + 1] - digits[i] != diff:
                is_hansu = False
                break
        if is_hansu:
            answer += 1

print(answer)
