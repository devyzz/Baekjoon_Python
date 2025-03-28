# 신용카드는 총 16자리의 숫자로 구성되어 있다. 언뜻 보기에는 무작위로 된 숫자로 구성되어 있는 것 같이 보이지만 그 속에는 하나의 수학적 비밀이 숨겨져 있다.
# 그중 하나가 카드 번호가 유효 한지 유효하지 않은 지 검사하는 Luhn 공식이다. 그 공식은 다음과 같다.

# ㄴ신용카드의 16자리 숫자에서 맨 우측 수부터 세어 홀수 번째 수는 그대로 두고, 짝수 번째 수를 2배로 만든다.
# ㄴ2배로 만든 짝수 번째 수가 10 이상인 경우, 각 자리의 숫자를 더하고 그 수로 대체한다.
# ㄴ이와 같이 얻은 모든 자리의 수를 더한다.
# ㄴ그 합이 10으로 나뉘면 “정당한 번호”(유효)이고 그렇지 않으면 “부당한 번호”(유효하지 않음)로 판정된다.

# 다음 공식을 이용해 주어진 신용카드의 번호가 유효한지, 유효하지 않은 지 판단해라.
import sys
N = int(input())

def trans_nubmers(number):
    total = 0
    l = len(number)
    for i in range(1,l+1):
        num = int(number[l-i])
        if i % 2 == 0:
            tmp = num * 2
            if tmp >= 10:
                total += (tmp//10) + (tmp%10)
            else:
                total += tmp
        else:
            total += num

    if total % 10 == 0:
        return 'T'
    else:
        return 'F'

credits = [sys.stdin.readline().strip() for _ in range(N)]

for credit in credits:
    print(trans_nubmers(credit))


