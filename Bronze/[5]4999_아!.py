# 입력은 두 줄로 이루어져 있다. 첫째 줄은 재환이가 가장 길게 낼 수 있는 "aaah"이다. 둘째 줄은 의사가 듣기를 원하는 "aah"이다.
# 두 문자열은 모두 a와 h로만 이루어져 있다. a의 개수는 0보다 크거나 같고, 999보다 작거나 같으며, 항상 h는 마지막에 하나만 주어진다.

# 재환이가 그 병원에 가야하면 "go"를, 아니면 "no"를 출력한다.

import sys

me = sys.stdin.readline()
doc = sys.stdin.readline()

me = len(me[:-1])
doc = len(doc[:-1])

print ("no" if me < doc else "go")