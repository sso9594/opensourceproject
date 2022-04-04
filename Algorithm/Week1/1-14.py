num = int(input("*를 출력합니다. \n몇개를 출력할까요?: "))
space = int(input("몇 개마다 줄바꿈할까요?: "))


for i in range(num):
    print("*", end="")
    if i % space == space - 1:
        print()

# 문제점: for문 반복 n번
# if 판단도 n번 수행
