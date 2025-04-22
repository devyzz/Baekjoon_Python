# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

expression = input().strip()

if '-' in expression:
    first_part, second_part = expression.split('-', 1)
    result = sum(map(int, first_part.split('+'))) - sum(map(int, second_part.replace('-', '+').split('+')))
else:
    result = sum(map(int, expression.split('+')))

print(result)
