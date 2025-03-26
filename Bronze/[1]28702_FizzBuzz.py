# i가 3의 배수 이면서 5의 배수면 FizzBuzz
# i가 3의 배수 지만 5의 배수가 아니면 Fizz
# i가 3의 배수가 아니지만 5의 배수면 Buzz
# i가 3의 배수도 아니고 5의 배수도 아닌 경우 i 출력

# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다.
# 각 문자열의 길이는 8이하입니다. 입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.
import sys

words = [sys.stdin.readline().strip() for _ in range(3)]
answer = 0

def check_number(num):
    answer = ''
    if num % 3 == 0 and num % 5 == 0:
        answer = "FizzBuzz"
    elif num % 3 == 0:
        answer = "Fizz"
    elif num % 5 == 0:
        answer = "Buzz"
    else:
        answer = num
    return answer

for i, word in enumerate(words):
    if word not in ['Fizz', 'Buzz', 'FizzBuzz']:
        answer = int(word) + 3 - i

print(check_number(answer))

