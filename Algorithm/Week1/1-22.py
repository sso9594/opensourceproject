# 왼쪽 아래가 직각이등변인 삼각형 *로 출력

num = int(input("왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.\n짧은 변의 길이를 입력하세요.: "))

for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print(" ")
