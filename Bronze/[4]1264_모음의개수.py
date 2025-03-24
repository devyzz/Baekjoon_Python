# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오.
# 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

import sys

vowels = 'aeiou'
target_str = ''

while True:
    count = 0
    target_str = sys.stdin.readline().strip().lower()
    if target_str == '#':
        break
    else:
        for char in vowels:
            char_cnt = target_str.count(char)
            count += char_cnt
        print(count)
