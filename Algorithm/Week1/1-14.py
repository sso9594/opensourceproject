num = int(input("*를 출력합니다. \n몇개를 출력할까요?: "))
space = int(input("몇 개마다 줄바꿈할까요?: "))

# 별 갯수 = 10
# 스페이스값 = 3

for i in range(num):
    # 인덱스는 0부터 시작하기 때문에 배수 성질에다가 -1해 줌
    print("*", end="")
    if i % space == space - 1:
        print()

if num % space:
    print()
