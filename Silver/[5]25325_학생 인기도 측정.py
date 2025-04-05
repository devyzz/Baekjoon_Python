# 학생 이름이 공백으로 구분된 문자열 A가 주어진다. 문자열 A에는 중복된 학생 이름이 존재하지 않는다. 학생 이름은 알파벳 소문자로 이루어져 있다.
# 각 학생이 좋아하는 학생의 학생 이름 목록이 공백으로 구분된 문자열로 주어진다. 각 학생이 좋아하는 학생은 1명 이상 주어지고, 내가 나를 좋아하는 예는 없다.
# 나를 좋아하는 학생이 많을수록 나의 인기도가 높다. 인기도가 높은 학생부터 낮은 학생 순으로 학생 이름과 해당 학생을 좋아하는 학생 수를 출력하자.
# 인기도가 같은 경우 학생 이름 기준으로 오름차순으로 출력하자.

n = int(input())
keys = input().split()
students = {key:0 for key in keys}

for _ in range(n):
    people = input().split()
    for person in people:
        students[person] += 1

results = dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))

for key,value in results.items():
    print(key,value)