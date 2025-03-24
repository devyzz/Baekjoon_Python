# 텍스트에서 줄을 입력받은 뒤, 줄 번호를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 줄의 수 N이 주어진다. 둘째 줄부터 N개의 줄에 각 줄의 내용이 주어진다.
# 각 줄에 있는 글자의 개수는 50글자를 넘지 않는다.
import sys

N = int(input())
str_list = []

for i in range(N):
    input_str = sys.stdin.readline()
    str_list.append(input_str)

for i in range(N):
    print(f"{i+1}. {str_list[i]}", end="")