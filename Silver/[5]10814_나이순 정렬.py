# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
import sys

N = int(input())
members = [sys.stdin.readline().strip() for _ in range(N)]
print(members)

# (나이, 가입 순서) 튜플을 함께 저장
members = [(int(member.split(' ')[0]), i, member) for i, member in enumerate(members)]
print(members)

# 나이 오름차순 → 가입 순서 오름차순 정렬
sorted_members = sorted(members, key=lambda x: (x[0], x[1]))

# 원래 문자열만 출력
for _, _, member in sorted_members:
    print(member)
