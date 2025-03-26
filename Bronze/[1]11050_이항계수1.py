#자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.
import math

n, k = map(int, input().split())
answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print(answer)