# 페르마의 마지막 정리는, a, b, c가 0이 아닌 정수이고, n이 2보다 큰 자연수 일 때,
# an = bn + cn을 만족하는 자연수 a, b, c가 존재하지 않는다는 정리이다. 이 정리는 아직 증명되지 않았다.
# 하지만, 완전 세제곱 방정식 a3 = b3 + c3 + d3을 만족하는 1보다 큰 자연수를 찾는 것은 어렵지 않다. (123 = 63 + 83 + 103)
# 이러한 완전 세제곱 방정식과 a ≤ 100을 만족하는 {a, b, c, d}쌍을 모두 찾는 프로그램을 작성하시오.

for a in range(2,101):
    for b in range(2,101):
        for c in range(b+1,101):
            for d in range(c+1,101):
                if a*a*a==(b*b*b+c*c*c+d*d*d):
                    print("Cube = {}, Triple = ({},{},{})".format(a,b,c,d))
                if a*a*a<(b*b*b+c*c*c+d*d*d):break
