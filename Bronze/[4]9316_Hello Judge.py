# 당신은 N개의 테스트케이스들에게 반드시 인사를 해야 이 문제를 풀 수 있다.
# N개의 줄에 걸쳐"Hello World, Judge i!"를 출력하는 프로그램을 만들라. 여기서 i는 줄의 번호이다.

N = int(input())
for i in range(N):
    print(f"Hello World, Judge {i+1}!")