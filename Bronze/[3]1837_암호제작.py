# 원룡이는 한 컴퓨터 보안 회사에서 일을 하고 있다. 그러던 도중, 원룡이는 YESWOA.COM 으로부터 홈페이지 유저들의 비밀키를 만들라는 지시를 받았다. 원룡이는 비밀 키를 다음과 같은 방법으로 만들었다.
# 개인마다 어떤 특정한 소수 p와 q를 주어 두 소수의 곱 pq를 비밀 키로 두었다. 이렇게 해 주면 두 소수 p,q를 알지 못하는 이상, 비밀 키를 알 수 없다는 장점을 가지고 있다.
# 하지만 원룡이는 한 가지 사실을 잊고 말았다. 최근 컴퓨터 기술이 발달함에 따라, 소수가 작은 경우에는 컴퓨터로 모든 경우의 수를 돌려보아 비밀 키를 쉽게 알 수 있다는 것이다.
# 원룡이는 주성조교님께 비밀 키를 제출하려던 바로 직전에 이 사실을 알아냈다. 그래서 두 소수 p, q 중 하나라도 K보다 작은 암호는 좋지 않은 암호로 간주하여 제출하지 않기로 하였다. 이것을 손으로 직접 구해보는 일은 매우 힘들 것이다. 당신은 원룡이를 도와 두 소수의 곱으로 이루어진 암호와 K가 주어져 있을 때, 그 암호가 좋은 암호인지 좋지 않은 암호인지 구하는 프로그램을 작성하여야 한다

def sieve(limit):
    is_prime = [True] * limit
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

def check_password(P, K):
    primes = sieve(K)
    for prime in primes:
        if P % prime == 0:
            print(f"BAD {prime}")
            return
    print("GOOD")

# 입력 처리
P_str, K_str = input().split()
P = int(P_str)
K = int(K_str)
check_password(P, K)
