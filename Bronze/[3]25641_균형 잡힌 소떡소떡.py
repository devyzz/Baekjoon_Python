# 소떡소떡은 기다란 꼬치에 소세지와 떡을 끼운 음식이다. 편의상 소떡소떡을 알파벳 s와 t로만 구성된 길이
# $N$의 문자열로 생각하자. 알파벳 s는 소세지를, t는 떡을 의미한다.

N = int(input())
word = input()

answer = ''
for i in range(N):
    tmp = word[i:N]
    if tmp.count('s') == tmp.count('t'):
        answer = tmp
        break

print(answer)