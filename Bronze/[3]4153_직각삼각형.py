import sys

answer = ""
while True:
    angles = list(map(int, sys.stdin.readline().split(' ')))
    if angles[0] == 0:
        break
    angles.sort()
    if angles[2] ** 2 == angles[0] ** 2 + angles[1] ** 2:
        answer += "right\n"
    else:
        answer += "wrong\n"

print(answer)


