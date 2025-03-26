## 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

x, y = map(int,input().split())

def gcd_mod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

def lcm(a,b,gcd):
    return a * b // gcd

gcd = gcd_mod(x,y)
lcm = lcm(x,y,gcd)

print(gcd)
print(lcm)