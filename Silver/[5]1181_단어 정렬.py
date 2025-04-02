# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys

N = int(sys.stdin.readline().rstrip())
word_set = set()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    word_set.add(word)

sorted_set = sorted(word_set, key=lambda x: (len(x), x))
print("\n".join(sorted_set))
