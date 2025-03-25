# 첫째 줄에 정수 N이 주어집니다.
# "SciComLove"를 N번 뒤집은 문자열을 출력합니다. 단, 따옴표는 출력하지 않습니다.

num = int(input())  # 정수 입력받기

if num % 2 == 0:
    print("SciComLove")  # 짝수일 경우
else:
    print("evoLmoCicS")  # 홀수일 경우
