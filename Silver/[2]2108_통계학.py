# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

import sys
from collections import Counter

N = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 산술평균 구하기
avg = round(sum(numbers) / len(numbers))
print(avg)

# 중앙값 구하기
numbers.sort()
mid= numbers[N//2]
print(mid)

# 최빈값 구하기
counter = Counter(numbers)
oft = 0
if len(numbers) > 1:
    cnt = Counter(numbers).most_common(2)
    if cnt[0][1] == cnt[1][1]:
        oft = cnt[1][0]
    else:
        oft = cnt[0][0]
else:
    cnt = Counter(numbers).most_common(1)
    oft = cnt[0][0]

print(oft)

# 범위구하기
dif = numbers[N-1] - numbers[0]
print(dif)