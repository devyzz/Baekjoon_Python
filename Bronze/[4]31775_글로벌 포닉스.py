#포닉스의 빅데이터 연구 결과, 세 문자열이 순서와 관계없이 각각 l, k, p로 시작할 경우 포스텍은 ICPC World Finals에 진출할 수 있다.
# 포닉스는 이러한 응원 문구를 GLOBAL한 문구로 부르기로 했다.
# 포닉스가 정한 세 개의 문자열이 주어질 때, 응원 문구가 GLOBAL한지 판단하여라.

answer = 'GLOBAL'
words = ['l', 'k', 'p']

for i in range(3):
    string = input()
    if string[0] not in words:  # 첫 번째 글자가 'l', 'k', 'p'가 아니면
        answer = 'PONIX'
    else:
        words.remove(string[0])
print(answer)

