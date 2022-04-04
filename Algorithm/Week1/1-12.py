# 특정 문자를 줄바꿈없이 번갈아 출력함

num = int(input("+와 -를 번갈아 출력합니다. \n몇 개를 출력할까요?: "))

for i in range(num):
    # 홀수인 경우 - 출력
    if i % 2 == 1:
        print("-", end="")
    # 짝수인 경우 + 출력
    else:
        print("+", end="")
