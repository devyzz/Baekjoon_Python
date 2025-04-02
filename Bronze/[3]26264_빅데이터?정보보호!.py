# 빅데이터·정보보호학과에서 수업을 하던 노교수는 학생들이 빅데이터와 정보보호 중 어느 분야에 더 관심이 많은지 궁금해졌다.
# 그래서 학생들을 만날 때마다 항상 이를 물어보고 답을 bigdata 혹은 security로 구분하여 메모장에 적어두었는데,
# 실수로 띄어쓰기와 개행이 전혀 없는 상태로 기록해두었다.
# 이대로는 학생들이 빅데이터와 정보보호 중 어느 분야에 더 관심이 많은지를 알아낼 수 없기 때문에, 당신에게 분석을 의뢰했다.
# 물어본 학생의 수와 답이 주어질 때, 결과를 출력하자.
# 첫 번째 줄에 정보보호 분야보다 빅데이터 분야에 관심이 있는 학생이 더 많으면 "bigdata?"를,
# 빅데이터 분야보다 정보보호 분야에 관심이 있는 학생이 더 많으면 "security!"를, 같으면 "bigdata? security!"를 따옴표 없이 출력한다.
N = int(input())
sentence = input()

s_cnt = 0
b_cnt = 0
while len(sentence) != 0:
    start = sentence[0]
    if start == 's':
        s_cnt += 1
        sentence = sentence[8:]
    else:
        b_cnt += 1
        sentence = sentence[7:]

if s_cnt > b_cnt:
    print("security!")
elif s_cnt < b_cnt:
    print("bigdata?")
else:
    print("bigdata? security!")