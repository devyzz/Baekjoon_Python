import math

N = int(input())  # 입력받을 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트

answer = 0
for number in numbers:
    if number > 1:  # 1은 소수가 아니므로 제외
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):  # 2부터 number의 제곱근까지 검사
            if number % i == 0:  # 나누어 떨어지면 소수가 아님
                is_prime = False
                break
        if is_prime:  # 소수일 경우
            answer += 1

print(answer)