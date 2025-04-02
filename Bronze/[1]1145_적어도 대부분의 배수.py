# 다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.
# 서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

def min_divisible_number(nums):
    n = 1
    while True:
        count = sum(n % num == 0 for num in nums)  # n을 나눌 수 있는 숫자의 개수 계산
        if count >= 3:  # 적어도 세 개의 숫자로 나누어지는지 확인
            return n
        n += 1

# 입력 처리
nums = list(map(int, input().split()))
print(min_divisible_number(nums))
