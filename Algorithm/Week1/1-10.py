# a부터 b까지 정수의 합을 구하는 과정과 최종값을 출력

print("a부터 b까지 정수의 합을 구합니다")
a = int(input("정수 a를 입력하세요: "))
b = int(input("정수 b를 입력하세요: "))

# 정수의 합 구하는 과정과 최종값 출력 알고리즘

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b+1):
    if i < b:
        print("{} +".format(i), end=" ")
    else:
        print("{} = ".format(i), end=" ")

    sum += i

print(sum)
