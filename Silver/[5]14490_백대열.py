# 대열이는 욱제의 친구다.
#
# “야 백대열을 약분하면 뭔지 알아?”
# “??”
# “십대일이야~ 하하!”
# n:m이 주어진다. 욱제를 도와주자. (...)

# 두 수를 최대한으로 약분하여 출력한다.
import sys

#최대공약수 찾기
def find_gd(a,b):
    while min(a,b)!=0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return max(a,b)

n,m = map(int, sys.stdin.readline().rstrip().split(":"))
gd = find_gd(n,m)
print(f"{n//gd}:{m//gd}")
