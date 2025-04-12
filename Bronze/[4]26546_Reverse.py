# String 클래스에는 substring이라는 함수가 있습니다. substring 함수의 반대 역할을 하는 것입니다.
# 문자열 내에서 지정된 부분 문자열을 반환하는 대신, 부분 문자열을 제거한 문자열을 출력합니다.


for _ in range(int(input())) :
    s, i, j = input().split()
    for x in range(int(i)) :
        print(s[x], end = "")
    for x in range(int(j), len(s)) :
        print(s[x], end = "")
    print()
