# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.
#
# 삼각형의 세 각을 입력받은 다음,
#
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.

angles = []

for i in range(3):
    angles.append(int(input()))

if sum(angles) != 180:
    print("Error")
else:
    unique_angles = len(set(angles))  # 중복을 제거한 고유 각의 개수를 구함
    if unique_angles == 1:
        print("Equilateral")
    elif unique_angles == 2:
        print("Isosceles")
    else:
        print("Scalene")

