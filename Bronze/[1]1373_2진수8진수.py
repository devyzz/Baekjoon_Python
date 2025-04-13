# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

binary = input()

# 3의 배수 길이가 되도록 앞에 0을 채움
while len(binary) % 3 != 0:
    binary = '0' + binary

result = ''
# 3자리씩 잘라서 8진수로 변환
for i in range(0, len(binary), 3):
    three_bits = binary[i:i+3]
    result += str(int(three_bits, 2))  # 2진수를 10진수로 변환 후 문자열로 저장

print(result)