# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

import time

def max_subarray_brute_force(a):
    n = len(a)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

def max_subarray_prefix_sum(a):
    n = len(a)
    p = [0] * (n + 1)

    for i in range(n):
        p[i+1] = p[i] + a[i]

    max_sum = float('-inf')
    for i in range(n):
        for j in range(i+1, n+1):
            sub_sum = p[j] - p[i]
            max_sum = max(max_sum, sub_sum)

    return max_sum

def max_crossing_sum(a, left, mid, right):
    left_sum = float('-inf')
    temp_sum = 0
    for i in range(mid, left - 1, -1):
        temp_sum += a[i]
        left_sum = max(left_sum, temp_sum)

    right_sum = float('-inf')
    temp_sum = 0
    for i in range(mid + 1, right + 1):
        temp_sum += a[i]
        right_sum = max(right_sum, temp_sum)

    return left_sum + right_sum

def max_subarray_divide_and_conquer(a, left, right):
    if left == right:
        return a[left]

    mid = (left + right) // 2
    left_max = max_subarray_divide_and_conquer(a, left, mid)
    right_max = max_subarray_divide_and_conquer(a, mid + 1, right)
    cross_max = max_crossing_sum(a, left, mid, right)

    return max(left_max, right_max, cross_max)

def max_subarray_dp(a):
    max_sum = current_sum = a[0]
    for i in range(1, len(a)):
        current_sum = max(a[i], current_sum + a[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

def run_and_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__}: 결과 = {result}, 실행시간 = {end - start:.6f}초")

def main():
    a = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

    print("최대 구간 합 알고리즘별 실행 시간 비교")
    print("=" * 40)

    run_and_time(max_subarray_brute_force, a)
    run_and_time(max_subarray_prefsix_sum, a)
    run_and_time(max_subarray_divide_and_conquer, a, 0, len(a) - 1)
    run_and_time(max_subarray_dp, a)

if __name__ == "__main__":
    main()
