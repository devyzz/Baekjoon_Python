# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

X = int(input())
str_arr = []

for i in range(X):
    a, b = map(int, sys.stdin.readline().split())
    str_arr.append(f"Case #{i+1}: {a} + {b} = {a+b}")

for i in range(X):
    print(str_arr[i])
