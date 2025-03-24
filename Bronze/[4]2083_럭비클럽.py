#올 골드 럭비 클럽의 회원들은 성인부 또는 청소년부로 분류된다.
# 나이가 17세보다 많거나, 몸무게가 80kg 이상이면 성인부이다. 그 밖에는 모두 청소년부이다. 클럽 회원들을 올바르게 분류하라.
#각 줄은 이름과 두 자연수로 이루어진다. 두 자연수는 순서대로 나이와 몸무게를 나타낸다.
# 입력의 마지막 줄은 # 0 0 이다. 이 입력은 처리하지 않는다.
#이름은 알파벳 대/소문자로만 이루어져 있고, 길이는 10을 넘지 않는다.

import sys

members = []
infos = []

while True:
    name, age, weight = sys.stdin.readline().split()
    if name == '#':
        break
    else:
        if int(age) > 17 or int(weight) >= 80:
            type='Senior'
        else:
            type='Junior'
        infos.append(name+" "+type)

for info in infos:
    print(info)